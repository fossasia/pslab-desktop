from __future__ import print_function

import time

import inspect
import serial

import PSL.commands_proto as CP


class Handler():
    def __init__(self, timeout=1.0, **kwargs):
        self.burstBuffer = b''
        self.loadBurst = False
        self.inputQueueSize = 0
        self.BAUD = 1000000
        self.timeout = timeout
        self.version_string = b''
        self.connected = False
        self.fd = None
        self.expected_version1 = b'CS'
        self.expected_version2 = b'PS'
        self.occupiedPorts = set()
        self.blockingSocket = None
        if 'port' in kwargs:
            self.portname = kwargs.get('port', None)
            try:
                self.fd, self.version_string, self.connected = self.connectToPort(self.portname)
                if self.connected: return
            except Exception as ex:
                print('Failed to connect to ', self.portname, ex.message)

        else:  # Scan and pick a port
            L = self.listPorts()
            for a in L:
                try:
                    self.portname = a
                    self.fd, self.version_string, self.connected = self.connectToPort(self.portname)
                    if self.connected:
                        print(a + ' .yes.', self.version_string)
                        return
                except:
                    pass
            if not self.connected:
                if len(self.occupiedPorts): print('Device not found. Programs already using :', self.occupiedPorts)

    def listPorts(self):
        import platform, glob
        system_name = platform.system()
        if system_name == "Windows":
            # Scan for available ports.
            available = []
            for i in range(256):
                try:
                    portname = 'COM' + str(i)
                    s = serial.Serial(portname)
                    available.append(portname)
                    s.close()
                except serial.SerialException:
                    pass
            return available
        elif system_name == "Darwin":
            # Mac
            return glob.glob('/dev/tty*') + glob.glob('/dev/cu*')
        else:
            # Assume Linux or something else
            return glob.glob('/dev/ttyACM*') + glob.glob('/dev/ttyUSB*')

    def connectToPort(self, portname):
        import platform
        if platform.system() not in ["Windows", "Darwin"]:
            import socket
            try:
                self.blockingSocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                self.blockingSocket.bind('\0PSLab%s' % portname)
                self.blockingSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            except socket.error as e:
                self.occupiedPorts.add(portname)
                raise RuntimeError("Another program is using %s (%d)" % (portname))

        fd = serial.Serial(portname, 9600, stopbits=1, timeout=0.02)
        fd.read(100)
        fd.close()
        fd = serial.Serial(portname, self.BAUD, stopbits=1, timeout=1.0)
        if (fd.inWaiting()):
            fd.setTimeout(0.1)
            fd.read(1000)
            fd.flush()
            fd.setTimeout(1.0)
        version = self.get_version(fd)
        if version[:len(self.expected_version1)] == self.expected_version1 or version[:len(
                self.expected_version2)] == self.expected_version2:
            return fd, str(version)[1:], True

        return None, '', False

    def disconnect(self):
        if self.connected:
            self.fd.close()
        if self.blockingSocket:
            print('Releasing port')
            self.blockingSocket.shutdown(1)
            self.blockingSocket.close()
            self.blockingSocket = None

    def get_version(self, fd):
        fd.write(CP.COMMON)
        fd.write(CP.GET_VERSION)
        x = fd.readline()
        # print('remaining',[ord(a) for a in fd.read(10)])
        if len(x):
            x = x[:-1]
        return x

    def reconnect(self, **kwargs):
        if 'port' in kwargs:
            self.portname = kwargs.get('port', None)

        try:
            self.fd, self.version_string, self.connected = self.connectToPort(self.portname)
        except serial.SerialException as ex:
            msg = "failed to reconnect. Check device connections."
            print(msg)
            raise RuntimeError(msg)

    def __del__(self):
        # print('closing port')
        try:
            self.fd.close()
        except:
            pass

    def __get_ack__(self):
        """
        fetches the response byte
        1 SUCCESS
        2 ARGUMENT_ERROR
        3 FAILED
        used as a handshake
        """
        if not self.loadBurst:
            x = self.fd.read(1)
        else:
            self.inputQueueSize += 1
            return 1
        try:
            return CP.Byte.unpack(x)[0]
        except:
            return 3

    def __sendInt__(self, val):
        """
        transmits an integer packaged as two characters
        :params int val: int to send
        """
        if not self.loadBurst:
            self.fd.write(CP.ShortInt.pack(int(val)))
        else:
            self.burstBuffer += CP.ShortInt.pack(int(val))

    def __sendByte__(self, val):
        """
        transmits a BYTE
        val - byte to send
        """
        # print (val)
        if (type(val) == int):
            if not self.loadBurst:
                self.fd.write(CP.Byte.pack(val))
            else:
                self.burstBuffer += CP.Byte.pack(val)
        else:
            if not self.loadBurst:
                self.fd.write(val)
            else:
                self.burstBuffer += val

    def __getByte__(self):
        """
        reads a byte from the serial port and returns it
        """
        ss = self.fd.read(1)
        try:
            if len(ss):
                return CP.Byte.unpack(ss)[0]
        except Exception as ex:
            print('byte communication error.', time.ctime())
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)
            # sys.exit(1)

    def __getInt__(self):
        """
        reads two bytes from the serial port and
        returns an integer after combining them
        """
        ss = self.fd.read(2)
        try:
            if len(ss) == 2:
                return CP.ShortInt.unpack(ss)[0]
        except Exception as ex:
            print('int communication error.', time.ctime())
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)
            # sys.exit(1)

    def __getLong__(self):
        """
        reads four bytes.
        returns long
        """
        ss = self.fd.read(4)
        if len(ss) == 4:
            return CP.Integer.unpack(ss)[0]
        else:
            # print('.')
            return -1

    def waitForData(self, timeout=0.2):
        start_time = time.time()
        while time.time() - start_time < timeout:
            time.sleep(0.02)
            if self.fd.inWaiting(): return True
        return False

    def sendBurst(self):
        """
        Transmits the commands stored in the burstBuffer.
        empties input buffer
        empties the burstBuffer.

        The following example initiates the capture routine and sets OD1 HIGH immediately.

        It is used by the Transient response experiment where the input needs to be toggled soon
        after the oscilloscope has been started.

        >>> I.loadBurst=True
        >>> I.capture_traces(4,800,2)
        >>> I.set_state(I.OD1,I.HIGH)
        >>> I.sendBurst()


        """
        # print([Byte.unpack(a)[0] for a in self.burstBuffer],self.inputQueueSize)
        self.fd.write(self.burstBuffer)
        self.burstBuffer = ''
        self.loadBurst = False
        acks = self.fd.read(self.inputQueueSize)
        self.inputQueueSize = 0
        return [CP.Byte.unpack(a)[0] for a in acks]
