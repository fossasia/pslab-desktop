from __future__ import print_function
import PSL.commands_proto as CP
import numpy as np
import time, inspect


class I2C():
    """
    Methods to interact with the I2C port. An instance of Labtools.Packet_Handler must be passed to the init function


    Example::  Read Values from an HMC5883L 3-axis Magnetometer(compass) [GY-273 sensor] connected to the I2C port
        >>> ADDRESS = 0x1E
        >>> from PSL import sciencelab
        >>> I = sciencelab.connect()
        #Alternately, you may skip using I2C as a child instance of Interface,
        #and instead use I2C=PSL.Peripherals.I2C(PSL.packet_handler.Handler())

        # writing to 0x1E, set gain(0x01) to smallest(0 : 1x)
        >>> I.I2C.bulkWrite(ADDRESS,[0x01,0])

        # writing to 0x1E, set mode conf(0x02), continuous measurement(0)
        >>> I.I2C.bulkWrite(ADDRESS,[0x02,0])

        # read 6 bytes from addr register on I2C device located at ADDRESS
        >>> vals = I.I2C.bulkRead(ADDRESS,addr,6)

        >>> from numpy import int16
        #conversion to signed datatype
        >>> x=int16((vals[0]<<8)|vals[1])
        >>> y=int16((vals[2]<<8)|vals[3])
        >>> z=int16((vals[4]<<8)|vals[5])
        >>> print (x,y,z)

    """
    samples = 0
    total_bytes = 0
    channels = 0
    tg = 100
    MAX_SAMPLES = 10000

    def __init__(self, H):
        self.H = H
        from PSL import sensorlist
        self.SENSORS = sensorlist.sensors
        self.buff = np.zeros(10000)

    def init(self):
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_INIT)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def enable_smbus(self):
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_ENABLE_SMBUS)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def pullSCLLow(self, uS):
        """
        Hold SCL pin at 0V for a specified time period. Used by certain sensors such
        as MLX90316 PIR for initializing.

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        uS                  Time(in uS) to hold SCL output at 0 Volts
        ================    ============================================================================================

        """
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_PULLDOWN_SCL)
            self.H.__sendInt__(uS)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def config(self, freq, verbose=True):
        """
        Sets frequency for I2C transactions

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        freq                I2C frequency
        ================    ============================================================================================
        """
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_CONFIG)
            # freq=1/((BRGVAL+1.0)/64e6+1.0/1e7)
            BRGVAL = int((1. / freq - 1. / 1e7) * 64e6 - 1)
            if BRGVAL > 511:
                BRGVAL = 511
                if verbose: print('Frequency too low. Setting to :', 1 / ((BRGVAL + 1.0) / 64e6 + 1.0 / 1e7))
            self.H.__sendInt__(BRGVAL)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def start(self, address, rw):
        """
        Initiates I2C transfer to address via the I2C port

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        address             I2C slave address\n
        rw                  Read/write.
                            - 0 for writing
                            - 1 for reading.
        ================    ============================================================================================
        """
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_START)
            self.H.__sendByte__(((address << 1) | rw) & 0xFF)  # address
            return self.H.__get_ack__() >> 4
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def stop(self):
        """
        stops I2C transfer

        :return: Nothing
        """
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_STOP)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def wait(self):
        """
        wait for I2C

        :return: Nothing
        """
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_WAIT)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def send(self, data):
        """
        SENDS data over I2C.
        The I2C bus needs to be initialized and set to the correct slave address first.
        Use I2C.start(address) for this.

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        data                Sends data byte over I2C bus
        ================    ============================================================================================

        :return: Nothing
        """
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_SEND)
            self.H.__sendByte__(data)  # data byte
            return self.H.__get_ack__() >> 4
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def send_burst(self, data):
        """
        SENDS data over I2C. The function does not wait for the I2C to finish before returning.
        It is used for sending large packets quickly.
        The I2C bus needs to be initialized and set to the correct slave address first.
        Use start(address) for this.

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        data                Sends data byte over I2C bus
        ================    ============================================================================================

        :return: Nothing
        """
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_SEND_BURST)
            self.H.__sendByte__(data)  # data byte
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)
            # No handshake. for the sake of speed. e.g. loading a frame buffer onto an I2C display such as ssd1306

    def restart(self, address, rw):
        """
        Initiates I2C transfer to address

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        address             I2C slave address
        rw                  Read/write.
                            * 0 for writing
                            * 1 for reading.
        ================    ============================================================================================

        """
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_RESTART)
            self.H.__sendByte__(((address << 1) | rw) & 0xFF)  # address
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)
        return self.H.__get_ack__() >> 4

    def simpleRead(self, addr, numbytes):
        """
        Read bytes from I2C slave without first transmitting the read location.

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        addr                Address of I2C slave
        numbytes            Total Bytes to read
        ================    ============================================================================================
        """
        self.start(addr, 1)
        vals = self.read(numbytes)
        return vals

    def read(self, length):
        """
        Reads a fixed number of data bytes from I2C device. Fetches length-1 bytes with acknowledge bits for each, +1 byte
        with Nack.

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        length              number of bytes to read from I2C bus
        ================    ============================================================================================
        """
        data = []
        try:
            for a in range(length - 1):
                self.H.__sendByte__(CP.I2C_HEADER)
                self.H.__sendByte__(CP.I2C_READ_MORE)
                data.append(self.H.__getByte__())
                self.H.__get_ack__()
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_READ_END)
            data.append(self.H.__getByte__())
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)
        return data

    def read_repeat(self):
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_READ_MORE)
            val = self.H.__getByte__()
            self.H.__get_ack__()
            return val
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def read_end(self):
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_READ_END)
            val = self.H.__getByte__()
            self.H.__get_ack__()
            return val
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def read_status(self):
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_STATUS)
            val = self.H.__getInt__()
            self.H.__get_ack__()
            return val
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def readBulk(self, device_address, register_address, bytes_to_read):
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_READ_BULK)
            self.H.__sendByte__(device_address)
            self.H.__sendByte__(register_address)
            self.H.__sendByte__(bytes_to_read)
            data = self.H.fd.read(bytes_to_read)
            self.H.__get_ack__()
            try:
                return [ord(a) for a in data]
            except:
                print('Transaction failed')
                return False
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def writeBulk(self, device_address, bytestream):
        """
        write bytes to I2C slave

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        device_address      Address of I2C slave
        bytestream          List of bytes to write
        ================    ============================================================================================
        """
        try:
            self.H.__sendByte__(CP.I2C_HEADER)
            self.H.__sendByte__(CP.I2C_WRITE_BULK)
            self.H.__sendByte__(device_address)
            self.H.__sendByte__(len(bytestream))
            for a in bytestream:
                self.H.__sendByte__(a)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def scan(self, frequency=100000, verbose=False):
        """
        Scan I2C port for connected devices

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        Frequency           I2C clock frequency
        ================    ============================================================================================

        :return: Array of addresses of connected I2C slave devices

        """

        self.config(frequency, verbose)
        addrs = []
        n = 0
        if verbose:
            print('Scanning addresses 0-127...')
            print('Address', '\t', 'Possible Devices')
        for a in range(0, 128):
            x = self.start(a, 0)
            if x & 1 == 0:  # ACK received
                addrs.append(a)
                if verbose: print(hex(a), '\t\t', self.SENSORS.get(a, 'None'))
                n += 1
            self.stop()
        return addrs

    def __captureStart__(self, address, location, sample_length, total_samples, tg):
        """
        Blocking call that starts fetching data from I2C sensors like an oscilloscope fetches voltage readings
        You will then have to call `__retrievebuffer__` to fetch this data, and `__dataProcessor` to process and return separate channels
        refer to `capture` if you want a one-stop solution.
        
        .. tabularcolumns:: |p{3cm}|p{11cm}|
        ==================  ============================================================================================
        **Arguments**
        ==================  ============================================================================================
        address             Address of the I2C sensor
        location            Address of the register to read from
        sample_length       Each sample can be made up of multiple bytes startng from <location> . such as 3-axis data
        total_samples       Total samples to acquire. Total bytes fetched = total_samples*sample_length
        tg                  timegap between samples (in uS)
        ==================  ============================================================================================

        :return: Arrays X(timestamps),Y1,Y2 ...

        """
        if (tg < 20): tg = 20
        total_bytes = total_samples * sample_length
        print('total bytes calculated : ', total_bytes)
        if (total_bytes > self.MAX_SAMPLES * 2):
            print('Sample limit exceeded. 10,000 int / 20000 bytes total')
            total_bytes = self.MAX_SAMPLES * 2
            total_samples = total_bytes / sample_length  # 2* because sample array is in Integers, and we're using it to store bytes

        print('length of each channel : ', sample_length)
        self.total_bytes = total_bytes
        self.channels = sample_length
        self.samples = total_samples
        self.tg = tg

        self.H.__sendByte__(CP.I2C_HEADER)
        self.H.__sendByte__(CP.I2C_START_SCOPE)
        self.H.__sendByte__(address)
        self.H.__sendByte__(location)
        self.H.__sendByte__(sample_length)
        self.H.__sendInt__(total_samples)  # total number of samples to record
        self.H.__sendInt__(tg)  # Timegap between samples.  1MHz timer clock
        self.H.__get_ack__()
        return 1e-6 * self.samples * self.tg + .01

    def __retrievebuffer__(self):
        '''
        Fetch data acquired by the I2C scope. refer to :func:`__captureStart__`
        '''
        total_int_samples = self.total_bytes / 2
        DATA_SPLITTING = 500
        print('fetchin samples : ', total_int_samples, '   split', DATA_SPLITTING)
        data = b''
        for i in range(int(total_int_samples / DATA_SPLITTING)):
            self.H.__sendByte__(CP.ADC)
            self.H.__sendByte__(CP.GET_CAPTURE_CHANNEL)
            self.H.__sendByte__(0)  # starts with A0 on PIC
            self.H.__sendInt__(DATA_SPLITTING)
            self.H.__sendInt__(i * DATA_SPLITTING)
            rem = DATA_SPLITTING * 2 + 1
            for _ in range(200):
                partial = self.H.fd.read(
                    rem)  # reading int by int sometimes causes a communication error. this works better.
                rem -= len(partial)
                data += partial
                # print ('partial: ',len(partial), end=",")
                if rem <= 0:
                    break
            data = data[:-1]
            # print ('Pass : len=',len(data), ' i = ',i)

        if total_int_samples % DATA_SPLITTING:
            self.H.__sendByte__(CP.ADC)
            self.H.__sendByte__(CP.GET_CAPTURE_CHANNEL)
            self.H.__sendByte__(0)  # starts with A0 on PIC
            self.H.__sendInt__(total_int_samples % DATA_SPLITTING)
            self.H.__sendInt__(total_int_samples - total_int_samples % DATA_SPLITTING)
            rem = 2 * (total_int_samples % DATA_SPLITTING) + 1
            for _ in range(20):
                partial = self.H.fd.read(
                    rem)  # reading int by int sometimes causes a communication error. this works better.
                rem -= len(partial)
                data += partial
                # print ('partial: ',len(partial), end="")
                if rem <= 0:
                    break
            data = data[:-1]
        print('Final Pass : len=', len(data))
        return data

    def __dataProcessor__(self, data, *args):
        '''
        Interpret data acquired by the I2C scope. refer to :func:`__retrievebuffer__` to fetch data
        
        ==================  ============================================================================================
        **Arguments**
        ==================  ============================================================================================
        data                byte array returned by :func:`__retrievebuffer__`
        *args               supply optional argument 'int' if consecutive bytes must be combined to form short integers
        ==================  ============================================================================================

        '''

        try:
            data = [ord(a) for a in data]
            if ('int' in args):
                for a in range(self.channels * self.samples / 2): self.buff[a] = np.int16(
                    (data[a * 2] << 8) | data[a * 2 + 1])
            else:
                for a in range(self.channels * self.samples): self.buff[a] = data[a]

            yield np.linspace(0, self.tg * (self.samples - 1), self.samples)
            for a in range(int(self.channels / 2)):
                yield self.buff[a:self.samples * self.channels / 2][::self.channels / 2]
        except Exception as ex:
            msg = "Incorrect number of bytes received", ex
            raise RuntimeError(msg)

    def capture(self, address, location, sample_length, total_samples, tg, *args):
        """
        Blocking call that fetches data from I2C sensors like an oscilloscope fetches voltage readings

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ==================  ============================================================================================
        **Arguments**
        ==================  ============================================================================================
        address             Address of the I2C sensor
        location            Address of the register to read from
        sample_length       Each sample can be made up of multiple bytes startng from <location> . such as 3-axis data
        total_samples       Total samples to acquire. Total bytes fetched = total_samples*sample_length
        tg                  timegap between samples (in uS)
        ==================  ============================================================================================

        Example

        >>> from pylab import *
        >>> I=sciencelab.ScienceLab()
        >>> x,y1,y2,y3,y4 = I.capture_multiple(800,1.75,'CH1','CH2','MIC','SEN')
        >>> plot(x,y1)
        >>> plot(x,y2)
        >>> plot(x,y3)
        >>> plot(x,y4)
        >>> show()

        :return: Arrays X(timestamps),Y1,Y2 ...

        """
        t = self.__captureStart__(address, location, sample_length, total_samples, tg)
        time.sleep(t)
        data = self.__retrievebuffer__()
        return self.__dataProcessor__(data, *args)


class SPI():
    """
    Methods to interact with the SPI port. An instance of Packet_Handler must be passed to the init function

    """

    def __init__(self, H):
        self.H = H

    def set_parameters(self, primary_prescaler=0, secondary_prescaler=2, CKE=1, CKP=0, SMP=1):
        """
        sets SPI parameters.

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        primary_pres        Primary Prescaler(0,1,2,3) for 64MHz clock->(64:1,16:1,4:1,1:1)
        secondary_pres      Secondary prescaler(0,1,..7)->(8:1,7:1,..1:1)
        CKE                 CKE 0 or 1.
        CKP                 CKP 0 or 1.
        ================    ============================================================================================

        """
        try:
            self.H.__sendByte__(CP.SPI_HEADER)
            self.H.__sendByte__(CP.SET_SPI_PARAMETERS)
            # 0Bhgfedcba - > <g>: modebit CKP,<f>: modebit CKE, <ed>:primary pre,<cba>:secondary pre
            self.H.__sendByte__(secondary_prescaler | (primary_prescaler << 3) | (CKE << 5) | (CKP << 6) | (SMP << 7))
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def start(self, channel):
        """
        selects SPI channel to enable.
        Basically lowers the relevant chip select pin .

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        channel             1-7 ->[PGA1 connected to CH1,PGA2,PGA3,PGA4,PGA5,external chip select 1,external chip select 2]
                            8 -> sine1
                            9 -> sine2
        ================    ============================================================================================

        """
        try:
            self.H.__sendByte__(CP.SPI_HEADER)
            self.H.__sendByte__(CP.START_SPI)
            self.H.__sendByte__(channel)  # value byte
        # self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def set_cs(self, channel, state):
        """
        Enable or disable a chip select

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        channel             'CS1','CS2'
        state               1 for HIGH, 0 for LOW
        ================    ============================================================================================

        """
        try:
            channel = channel.upper()
            if channel in ['CS1', 'CS2']:
                csnum = ['CS1', 'CS2'].index(channel) + 9  # chip select number 9=CSOUT1,10=CSOUT2
                self.H.__sendByte__(CP.SPI_HEADER)
                if state:
                    self.H.__sendByte__(CP.STOP_SPI)
                else:
                    self.H.__sendByte__(CP.START_SPI)
                self.H.__sendByte__(csnum)
            else:
                print('Channel does not exist')
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def stop(self, channel):
        """
        selects SPI channel to disable.
        Sets the relevant chip select pin to HIGH.

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        channel             1-7 ->[PGA1 connected to CH1,PGA2,PGA3,PGA4,PGA5,external chip select 1,external chip select 2]
        ================    ============================================================================================


        """
        try:
            self.H.__sendByte__(CP.SPI_HEADER)
            self.H.__sendByte__(CP.STOP_SPI)
            self.H.__sendByte__(channel)  # value byte
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)
            # self.H.__get_ack__()

    def send8(self, value):
        """
        SENDS 8-bit data over SPI

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        value               value to transmit
        ================    ============================================================================================

        :return: value returned by slave device
        """
        try:
            self.H.__sendByte__(CP.SPI_HEADER)
            self.H.__sendByte__(CP.SEND_SPI8)
            self.H.__sendByte__(value)  # value byte
            v = self.H.__getByte__()
            self.H.__get_ack__()
            return v
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def send16(self, value):
        """
        SENDS 16-bit data over SPI

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        value               value to transmit
        ================    ============================================================================================

        :return: value returned by slave device
        :rtype: int
        """
        try:
            self.H.__sendByte__(CP.SPI_HEADER)
            self.H.__sendByte__(CP.SEND_SPI16)
            self.H.__sendInt__(value)  # value byte
            v = self.H.__getInt__()
            self.H.__get_ack__()
            return v
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def send8_burst(self, value):
        """
        SENDS 8-bit data over SPI
        No acknowledge/return value

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ================    ============================================================================================
        **Arguments**
        ================    ============================================================================================
        value               value to transmit
        ================    ============================================================================================

        :return: Nothing
        """
        try:
            self.H.__sendByte__(CP.SPI_HEADER)
            self.H.__sendByte__(CP.SEND_SPI8_BURST)
            self.H.__sendByte__(value)  # value byte
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def send16_burst(self, value):
        """
        SENDS 16-bit data over SPI
        no acknowledge/return value

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ==============  ============================================================================================
        **Arguments**
        ==============  ============================================================================================
        value           value to transmit
        ==============  ============================================================================================

        :return: nothing
        """
        try:
            self.H.__sendByte__(CP.SPI_HEADER)
            self.H.__sendByte__(CP.SEND_SPI16_BURST)
            self.H.__sendInt__(value)  # value byte
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def xfer(self, chan, data):
        self.start(chan)
        reply = []
        for a in data:
            reply.append(self.send8(a))
        self.stop(chan)
        return reply


class DACCHAN:
    def __init__(self, name, span, channum, **kwargs):
        self.name = name
        self.channum = channum
        self.VREF = kwargs.get('VREF', 0)
        self.SwitchedOff = kwargs.get('STATE', 0)
        self.range = span
        slope = (span[1] - span[0])
        intercept = span[0]
        self.VToCode = np.poly1d([4095. / slope, -4095. * intercept / slope])
        self.CodeToV = np.poly1d([slope / 4095., intercept])
        self.calibration_enabled = False
        self.calibration_table = []
        self.slope = 1
        self.offset = 0

    def load_calibration_table(self, table):
        self.calibration_enabled = 'table'
        self.calibration_table = table

    def load_calibration_twopoint(self, slope, offset):
        self.calibration_enabled = 'twopoint'
        self.slope = slope
        self.offset = offset

    # print('########################',slope,offset)

    def apply_calibration(self, v):
        if self.calibration_enabled == 'table':  # Each point is individually calibrated
            return int(np.clip(v + self.calibration_table[v], 0, 4095))
        elif self.calibration_enabled == 'twopoint':  # Overall slope and offset correction is applied
            # print (self.slope,self.offset,v)
            return int(np.clip(v * self.slope + self.offset, 0, 4095))
        else:
            return v


class MCP4728:
    defaultVDD = 3300
    RESET = 6
    WAKEUP = 9
    UPDATE = 8
    WRITEALL = 64
    WRITEONE = 88
    SEQWRITE = 80
    VREFWRITE = 128
    GAINWRITE = 192
    POWERDOWNWRITE = 160
    GENERALCALL = 0

    # def __init__(self,I2C,vref=3.3,devid=0):
    def __init__(self, H, vref=3.3, devid=0):
        self.devid = devid
        self.addr = 0x60 | self.devid  # 0x60 is the base address
        self.H = H
        self.I2C = I2C(self.H)
        self.SWITCHEDOFF = [0, 0, 0, 0]
        self.VREFS = [0, 0, 0, 0]  # 0=Vdd,1=Internal reference
        self.CHANS = {'PCS': DACCHAN('PCS', [0, 3.3e-3], 0), 'PV3': DACCHAN('PV3', [0, 3.3], 1),
                      'PV2': DACCHAN('PV2', [-3.3, 3.3], 2), 'PV1': DACCHAN('PV1', [-5., 5.], 3)}
        self.CHANNEL_MAP = {0: 'PCS', 1: 'PV3', 2: 'PV2', 3: 'PV1'}
        self.values = {'PV1': 0, 'PV2': 0, 'PV3': 0, 'PCS': 0}

    def __ignoreCalibration__(self, name):
        self.CHANS[name].calibration_enabled = False

    def setVoltage(self, name, v):
        chan = self.CHANS[name]
        v = int(round(chan.VToCode(v)))
        return self.__setRawVoltage__(name, v)

    def getVoltage(self, name):
        return self.values[name]

    def setCurrent(self, v):
        chan = self.CHANS['PCS']
        v = int(round(chan.VToCode(v)))
        return self.__setRawVoltage__('PCS', v)

    def __setRawVoltage__(self, name, v):
        v = int(np.clip(v, 0, 4095))
        CHAN = self.CHANS[name]
        '''
        self.H.__sendByte__(CP.DAC) #DAC write coming through.(MCP4728)
        self.H.__sendByte__(CP.SET_DAC)
        self.H.__sendByte__(self.addr<<1)	#I2C address
        self.H.__sendByte__(CHAN.channum)		#DAC channel
        if self.calibration_enabled[name]:
            val = v+self.calibration_tables[name][v]
            #print (val,v,self.calibration_tables[name][v])
            self.H.__sendInt__((CHAN.VREF << 15) | (CHAN.SwitchedOff << 13) | (0 << 12) | (val) )
        else:
            self.H.__sendInt__((CHAN.VREF << 15) | (CHAN.SwitchedOff << 13) | (0 << 12) | v )

        self.H.__get_ack__()
        '''
        val = self.CHANS[name].apply_calibration(v)
        self.I2C.writeBulk(self.addr, [64 | (CHAN.channum << 1), (val >> 8) & 0x0F, val & 0xFF])
        self.values[name] = CHAN.CodeToV(v)
        return self.values[name]

    def __writeall__(self, v1, v2, v3, v4):
        self.I2C.start(self.addr, 0)
        self.I2C.send((v1 >> 8) & 0xF)
        self.I2C.send(v1 & 0xFF)
        self.I2C.send((v2 >> 8) & 0xF)
        self.I2C.send(v2 & 0xFF)
        self.I2C.send((v3 >> 8) & 0xF)
        self.I2C.send(v3 & 0xFF)
        self.I2C.send((v4 >> 8) & 0xF)
        self.I2C.send(v4 & 0xFF)
        self.I2C.stop()

    def stat(self):
        self.I2C.start(self.addr, 0)
        self.I2C.send(0x0)  # read raw values starting from address
        self.I2C.restart(self.addr, 1)
        vals = self.I2C.read(24)
        self.I2C.stop()
        print(vals)


class NRF24L01():
    # Commands
    R_REG = 0x00
    W_REG = 0x20
    RX_PAYLOAD = 0x61
    TX_PAYLOAD = 0xA0
    ACK_PAYLOAD = 0xA8
    FLUSH_TX = 0xE1
    FLUSH_RX = 0xE2
    ACTIVATE = 0x50
    R_STATUS = 0xFF

    # Registers
    NRF_CONFIG = 0x00
    EN_AA = 0x01
    EN_RXADDR = 0x02
    SETUP_AW = 0x03
    SETUP_RETR = 0x04
    RF_CH = 0x05
    RF_SETUP = 0x06
    NRF_STATUS = 0x07
    OBSERVE_TX = 0x08
    CD = 0x09
    RX_ADDR_P0 = 0x0A
    RX_ADDR_P1 = 0x0B
    RX_ADDR_P2 = 0x0C
    RX_ADDR_P3 = 0x0D
    RX_ADDR_P4 = 0x0E
    RX_ADDR_P5 = 0x0F
    TX_ADDR = 0x10
    RX_PW_P0 = 0x11
    RX_PW_P1 = 0x12
    RX_PW_P2 = 0x13
    RX_PW_P3 = 0x14
    RX_PW_P4 = 0x15
    RX_PW_P5 = 0x16
    R_RX_PL_WID = 0x60
    FIFO_STATUS = 0x17
    DYNPD = 0x1C
    FEATURE = 0x1D
    PAYLOAD_SIZE = 0
    ACK_PAYLOAD_SIZE = 0
    READ_PAYLOAD_SIZE = 0

    ADC_COMMANDS = 1
    READ_ADC = 0 << 4

    I2C_COMMANDS = 2
    I2C_TRANSACTION = 0 << 4
    I2C_WRITE = 1 << 4
    I2C_SCAN = 2 << 4
    PULL_SCL_LOW = 3 << 4
    I2C_CONFIG = 4 << 4
    I2C_READ = 5 << 4

    NRF_COMMANDS = 3
    NRF_READ_REGISTER = 0
    NRF_WRITE_REGISTER = 1 << 4

    CURRENT_ADDRESS = 0xAAAA01
    nodelist = {}
    nodepos = 0
    NODELIST_MAXLENGTH = 15
    connected = False

    def __init__(self, H):
        self.H = H
        self.ready = False
        self.sigs = {self.CURRENT_ADDRESS: 1}
        if self.H.connected:
            self.connected = self.init()

    """
    routines for the NRFL01 radio
    """

    def init(self):
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_SETUP)
            self.H.__get_ack__()
            time.sleep(0.015)  # 15 mS settling time
            stat = self.get_status()
            if stat & 0x80:
                print("Radio transceiver not installed/not found")
                return False
            else:
                self.ready = True
            self.selectAddress(self.CURRENT_ADDRESS)
            # self.write_register(self.RF_SETUP,0x06)
            self.rxmode()
            time.sleep(0.1)
            self.flush()
            return True
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def rxmode(self):
        '''
        Puts the radio into listening mode.
        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_RXMODE)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def txmode(self):
        '''
        Puts the radio into transmit mode.
        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_TXMODE)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def triggerAll(self, val):
        self.txmode()
        self.selectAddress(0x111111)
        self.write_register(self.EN_AA, 0x00)
        self.write_payload([val], True)
        self.write_register(self.EN_AA, 0x01)

    def power_down(self):
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_POWER_DOWN)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def rxchar(self):
        '''
        Receives a 1 Byte payload
        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_RXCHAR)
            value = self.H.__getByte__()
            self.H.__get_ack__()
            return value
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def txchar(self, char):
        '''
        Transmits a single character
        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_TXCHAR)
            self.H.__sendByte__(char)
            return self.H.__get_ack__() >> 4
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def hasData(self):
        '''
        Check if the RX FIFO contains data
        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_HASDATA)
            value = self.H.__getByte__()
            self.H.__get_ack__()
            return value
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def flush(self):
        '''
        Flushes the TX and RX FIFOs
        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_FLUSH)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def write_register(self, address, value):
        '''
        write a  byte to any of the configuration registers on the Radio.
        address byte can either be located in the NRF24L01+ manual, or chosen
        from some of the constants defined in this module.
        '''
        # print ('writing',address,value)
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_WRITEREG)
            self.H.__sendByte__(address)
            self.H.__sendByte__(value)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def read_register(self, address):
        '''
        Read the value of any of the configuration registers on the radio module.

        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_READREG)
            self.H.__sendByte__(address)
            val = self.H.__getByte__()
            self.H.__get_ack__()
            return val
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def get_status(self):
        '''
        Returns a byte representing the STATUS register on the radio.
        Refer to NRF24L01+ documentation for further details
        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_GETSTATUS)
            val = self.H.__getByte__()
            self.H.__get_ack__()
            return val
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def write_command(self, cmd):
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_WRITECOMMAND)
            self.H.__sendByte__(cmd)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def write_address(self, register, address):
        '''
        register can be TX_ADDR, RX_ADDR_P0 -> RX_ADDR_P5
        3 byte address.  eg 0xFFABXX . XX cannot be FF
        if RX_ADDR_P1 needs to be used along with any of the pipes
        from P2 to P5, then RX_ADDR_P1 must be updated last.
        Addresses from P1-P5 must share the first two bytes.
        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_WRITEADDRESS)
            self.H.__sendByte__(register)
            self.H.__sendByte__(address & 0xFF)
            self.H.__sendByte__((address >> 8) & 0xFF)
            self.H.__sendByte__((address >> 16) & 0xFF)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def selectAddress(self, address):
        '''
        Sets RX_ADDR_P0 and TX_ADDR to the specified address.

        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_WRITEADDRESSES)
            self.H.__sendByte__(address & 0xFF)
            self.H.__sendByte__((address >> 8) & 0xFF)
            self.H.__sendByte__((address >> 16) & 0xFF)
            self.H.__get_ack__()
            self.CURRENT_ADDRESS = address
            if address not in self.sigs:
                self.sigs[address] = 1
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def read_payload(self, numbytes):
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_READPAYLOAD)
            self.H.__sendByte__(numbytes)
            data = self.H.fd.read(numbytes)
            self.H.__get_ack__()
            return [ord(a) for a in data]
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def write_payload(self, data, verbose=False, **args):
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_WRITEPAYLOAD)
            numbytes = len(
                data) | 0x80  # 0x80 implies transmit immediately. Otherwise it will simply load the TX FIFO ( used by ACK_payload)
            if (args.get('rxmode', False)): numbytes |= 0x40
            self.H.__sendByte__(numbytes)
            self.H.__sendByte__(self.TX_PAYLOAD)
            for a in data:
                self.H.__sendByte__(a)
            val = self.H.__get_ack__() >> 4
            if (verbose):
                if val & 0x2:
                    print(' NRF radio not found. Connect one to the add-on port')
                elif val & 0x1:
                    print(' Node probably dead/out of range. It failed to acknowledge')
                return
            return val
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def I2C_scan(self):
        '''
        Scans the I2C bus and returns a list of live addresses
        '''
        x = self.transaction([self.I2C_COMMANDS | self.I2C_SCAN | 0x80], timeout=500)
        if not x: return []
        if not sum(x): return []
        addrs = []
        for a in range(16):
            if (x[a] ^ 255):
                for b in range(8):
                    if x[a] & (0x80 >> b) == 0:
                        addr = 8 * a + b
                        addrs.append(addr)
        return addrs

    def GuessingScan(self):
        '''
        Scans the I2C bus and also prints the possible devices associated with each found address
        '''
        from PSL import sensorlist
        print('Scanning addresses 0-127...')
        x = self.transaction([self.I2C_COMMANDS | self.I2C_SCAN | 0x80], timeout=500)
        if not x: return []
        if not sum(x): return []
        addrs = []
        print('Address', '\t', 'Possible Devices')

        for a in range(16):
            if (x[a] ^ 255):
                for b in range(8):
                    if x[a] & (0x80 >> b) == 0:
                        addr = 8 * a + b
                        addrs.append(addr)
                        print(hex(addr), '\t\t', sensorlist.sensors.get(addr, 'None'))

        return addrs

    def transaction(self, data, **args):
        st = time.time()
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_TRANSACTION)
            self.H.__sendByte__(len(data))  # total Data bytes coming through
            if 'listen' not in args: args['listen'] = True
            if args.get('listen', False): data[0] |= 0x80  # You need this if hardware must wait for a reply
            timeout = args.get('timeout', 200)
            verbose = args.get('verbose', False)
            self.H.__sendInt__(timeout)  # timeout.
            for a in data:
                self.H.__sendByte__(a)

            # print ('dt send',time.time()-st,timeout,data[0]&0x80,data)
            numbytes = self.H.__getByte__()
            # print ('byte 1 in',time.time()-st)
            if numbytes:
                data = self.H.fd.read(numbytes)
            else:
                data = []
            val = self.H.__get_ack__() >> 4
            if (verbose):
                if val & 0x1: print(time.time(), '%s Err. Node not found' % (hex(self.CURRENT_ADDRESS)))
                if val & 0x2: print(time.time(),
                                    '%s Err. NRF on-board transmitter not found' % (hex(self.CURRENT_ADDRESS)))
                if val & 0x4 and args['listen']: print(time.time(),
                                                       '%s Err. Node received command but did not reply' % (
                                                           hex(self.CURRENT_ADDRESS)))
            if val & 0x7:  # Something didn't go right.
                self.flush()
                self.sigs[self.CURRENT_ADDRESS] = self.sigs[self.CURRENT_ADDRESS] * 50 / 51.
                return False

            self.sigs[self.CURRENT_ADDRESS] = (self.sigs[self.CURRENT_ADDRESS] * 50 + 1) / 51.
            return [ord(a) for a in data]
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def transactionWithRetries(self, data, **args):
        retries = args.get('retries', 5)
        reply = False
        while retries > 0:
            reply = self.transaction(data, verbose=(retries == 1), **args)
            if reply:
                break
            retries -= 1
        return reply

    def write_ack_payload(self, data, pipe):
        if (len(data) != self.ACK_PAYLOAD_SIZE):
            self.ACK_PAYLOAD_SIZE = len(data)
            if self.ACK_PAYLOAD_SIZE > 15:
                print('too large. truncating.')
                self.ACK_PAYLOAD_SIZE = 15
                data = data[:15]
            else:
                print('ack payload size:', self.ACK_PAYLOAD_SIZE)
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_WRITEPAYLOAD)
            self.H.__sendByte__(len(data))
            self.H.__sendByte__(self.ACK_PAYLOAD | pipe)
            for a in data:
                self.H.__sendByte__(a)
            return self.H.__get_ack__() >> 4
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def start_token_manager(self):
        '''
        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_START_TOKEN_MANAGER)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def stop_token_manager(self):
        '''
        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_STOP_TOKEN_MANAGER)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def total_tokens(self):
        '''
        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_TOTAL_TOKENS)
            x = self.H.__getByte__()
            self.H.__get_ack__()
            return x
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def fetch_report(self, num):
        '''
        '''
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_REPORTS)
            self.H.__sendByte__(num)
            data = [self.H.__getByte__() for a in range(20)]
            self.H.__get_ack__()
            return data
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def __decode_I2C_list__(self, data):
        lst = []
        if sum(data) == 0:
            return lst
        for a in range(len(data)):
            if (data[a] ^ 255):
                for b in range(8):
                    if data[a] & (0x80 >> b) == 0:
                        addr = 8 * a + b
                        lst.append(addr)
        return lst

    def get_nodelist(self):
        '''
        Refer to the variable 'nodelist' if you simply want a list of nodes that either registered while your code was
        running , or were loaded from the firmware buffer(max 15 entries)

        If you plan to use more than 15 nodes, and wish to register their addresses without having to feed them manually,
        then this function must be called each time before the buffer resets.

        The dictionary object returned by this function [addresses paired with arrays containing their registered sensors]
        is filtered by checking with each node if they are alive.

        '''

        total = self.total_tokens()
        if self.nodepos != total:
            for nm in range(self.NODELIST_MAXLENGTH):
                dat = self.fetch_report(nm)
                txrx = (dat[0]) | (dat[1] << 8) | (dat[2] << 16)
                if not txrx: continue
                self.nodelist[txrx] = self.__decode_I2C_list__(dat[3:19])
                self.nodepos = total
                # else:
                #	self.__delete_registered_node__(nm)

        filtered_lst = {}
        for a in self.nodelist:
            if self.isAlive(a): filtered_lst[a] = self.nodelist[a]

        return filtered_lst

    def __delete_registered_node__(self, num):
        try:
            self.H.__sendByte__(CP.NRFL01)
            self.H.__sendByte__(CP.NRF_DELETE_REPORT_ROW)
            self.H.__sendByte__(num)
            self.H.__get_ack__()
        except Exception as ex:
            self.raiseException(ex, "Communication Error , Function : " + inspect.currentframe().f_code.co_name)

    def __delete_all_registered_nodes__(self):
        while self.total_tokens():
            print('-')
            self.__delete_registered_node__(0)

    def isAlive(self, addr):
        self.selectAddress(addr)
        return self.transaction([self.NRF_COMMANDS | self.NRF_READ_REGISTER] + [self.R_STATUS], timeout=100,
                                verbose=False)

    def init_shockburst_transmitter(self, **args):
        '''
        Puts the radio into transmit mode.
        Dynamic Payload with auto acknowledge is enabled.
        upto 5 retransmits with 1ms delay between each in case a node doesn't respond in time
        Receivers must acknowledge payloads
        '''
        self.PAYLOAD_SIZE = args.get('PAYLOAD_SIZE', self.PAYLOAD_SIZE)
        myaddr = args.get('myaddr', 0xAAAA01)
        sendaddr = args.get('sendaddr', 0xAAAA01)

        self.init()
        # shockburst
        self.write_address(self.RX_ADDR_P0, myaddr)  # transmitter's address
        self.write_address(self.TX_ADDR, sendaddr)  # send to node with this address
        self.write_register(self.RX_PW_P0, self.PAYLOAD_SIZE)
        self.rxmode()
        time.sleep(0.1)
        self.flush()

    def init_shockburst_receiver(self, **args):
        '''
        Puts the radio into receive mode.
        Dynamic Payload with auto acknowledge is enabled.
        '''
        self.PAYLOAD_SIZE = args.get('PAYLOAD_SIZE', self.PAYLOAD_SIZE)
        if 'myaddr0' not in args:
            args['myaddr0'] = 0xA523B5
        # if 'sendaddr' non in args:
        #	args['sendaddr']=0xA523B5
        print(args)
        self.init()
        self.write_register(self.RF_SETUP, 0x26)  # 2MBPS speed

        # self.write_address(self.TX_ADDR,sendaddr)     #send to node with this address
        # self.write_address(self.RX_ADDR_P0,myaddr)	#will receive the ACK Payload from that node
        enabled_pipes = 0  # pipes to be enabled
        for a in range(0, 6):
            x = args.get('myaddr' + str(a), None)
            if x:
                print(hex(x), hex(self.RX_ADDR_P0 + a))
                enabled_pipes |= (1 << a)
                self.write_address(self.RX_ADDR_P0 + a, x)
        P15_base_address = args.get('myaddr1', None)
        if P15_base_address: self.write_address(self.RX_ADDR_P1, P15_base_address)

        self.write_register(self.EN_RXADDR, enabled_pipes)  # enable pipes
        self.write_register(self.EN_AA, enabled_pipes)  # enable auto Acknowledge on all pipes
        self.write_register(self.DYNPD, enabled_pipes)  # enable dynamic payload on Data pipes
        self.write_register(self.FEATURE, 0x06)  # enable dynamic payload length
        # self.write_register(self.RX_PW_P0,self.PAYLOAD_SIZE)

        self.rxmode()
        time.sleep(0.1)
        self.flush()


class RadioLink():
    ADC_COMMANDS = 1
    READ_ADC = 0 << 4

    I2C_COMMANDS = 2
    I2C_TRANSACTION = 0 << 4
    I2C_WRITE = 1 << 4
    SCAN_I2C = 2 << 4
    PULL_SCL_LOW = 3 << 4
    I2C_CONFIG = 4 << 4
    I2C_READ = 5 << 4

    NRF_COMMANDS = 3
    NRF_READ_REGISTER = 0 << 4
    NRF_WRITE_REGISTER = 1 << 4

    MISC_COMMANDS = 4
    WS2812B_CMD = 0 << 4

    def __init__(self, NRF, **args):
        self.NRF = NRF
        if 'address' in args:
            self.ADDRESS = args.get('address', False)
        else:
            print('Address not specified. Add "address=0x....." argument while instantiating')
            self.ADDRESS = 0x010101

    def __selectMe__(self):
        if self.NRF.CURRENT_ADDRESS != self.ADDRESS:
            self.NRF.selectAddress(self.ADDRESS)

    def I2C_scan(self):
        self.__selectMe__()
        from PSL import sensorlist
        print('Scanning addresses 0-127...')
        x = self.NRF.transaction([self.I2C_COMMANDS | self.SCAN_I2C | 0x80], timeout=500)
        if not x: return []
        if not sum(x): return []
        addrs = []
        print('Address', '\t', 'Possible Devices')

        for a in range(16):
            if (x[a] ^ 255):
                for b in range(8):
                    if x[a] & (0x80 >> b) == 0:
                        addr = 8 * a + b
                        addrs.append(addr)
                        print(hex(addr), '\t\t', sensorlist.sensors.get(addr, 'None'))

        return addrs

    def __decode_I2C_list__(self, data):
        lst = []
        if sum(data) == 0:
            return lst
        for a in range(len(data)):
            if (data[a] ^ 255):
                for b in range(8):
                    if data[a] & (0x80 >> b) == 0:
                        addr = 8 * a + b
                        lst.append(addr)
        return lst

    def writeI2C(self, I2C_addr, regaddress, bytes):
        self.__selectMe__()
        return self.NRF.transaction([self.I2C_COMMANDS | self.I2C_WRITE] + [I2C_addr] + [regaddress] + bytes)

    def readI2C(self, I2C_addr, regaddress, numbytes):
        self.__selectMe__()
        return self.NRF.transaction([self.I2C_COMMANDS | self.I2C_TRANSACTION] + [I2C_addr] + [regaddress] + [numbytes])

    def writeBulk(self, I2C_addr, bytes):
        self.__selectMe__()
        return self.NRF.transaction([self.I2C_COMMANDS | self.I2C_WRITE] + [I2C_addr] + bytes)

    def readBulk(self, I2C_addr, regaddress, numbytes):
        self.__selectMe__()
        return self.NRF.transactionWithRetries(
            [self.I2C_COMMANDS | self.I2C_TRANSACTION] + [I2C_addr] + [regaddress] + [numbytes])

    def simpleRead(self, I2C_addr, numbytes):
        self.__selectMe__()
        return self.NRF.transactionWithRetries([self.I2C_COMMANDS | self.I2C_READ] + [I2C_addr] + [numbytes])

    def readADC(self, channel):
        self.__selectMe__()
        return self.NRF.transaction([self.ADC_COMMANDS | self.READ_ADC] + [channel])

    def pullSCLLow(self, t_ms):
        self.__selectMe__()
        dat = self.NRF.transaction([self.I2C_COMMANDS | self.PULL_SCL_LOW] + [t_ms])
        if dat:
            return self.__decode_I2C_list__(dat)
        else:
            return []

    def configI2C(self, freq):
        self.__selectMe__()
        brgval = int(32e6 / freq / 4 - 1)
        print(brgval)
        return self.NRF.transaction([self.I2C_COMMANDS | self.I2C_CONFIG] + [brgval], listen=False)

    def write_register(self, reg, val):
        self.__selectMe__()
        # print ('writing to ',reg,val)
        return self.NRF.transaction([self.NRF_COMMANDS | self.NRF_WRITE_REGISTER] + [reg, val], listen=False)

    def WS2812B(self, cols):
        """
        set shade of WS2182 LED on CS1/RC0

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ==============  ============================================================================================
        **Arguments**
        ==============  ============================================================================================
        cols                2Darray [[R,G,B],[R2,G2,B2],[R3,G3,B3]...]
                            brightness of R,G,B ( 0-255  )
        ==============  ============================================================================================

        example::

            >>> WS2812B([[10,0,0],[0,10,10],[10,0,10]])
            #sets red, cyan, magenta to three daisy chained LEDs

        """
        self.__selectMe__()
        colarray = []
        for a in cols:
            colarray.append(int('{:08b}'.format(int(a[1]))[::-1], 2))
            colarray.append(int('{:08b}'.format(int(a[0]))[::-1], 2))
            colarray.append(int('{:08b}'.format(int(a[2]))[::-1], 2))

        res = self.NRF.transaction([self.MISC_COMMANDS | self.WS2812B_CMD] + colarray, listen=False)
        return res

    def read_register(self, reg):
        self.__selectMe__()
        x = self.NRF.transaction([self.NRF_COMMANDS | self.NRF_READ_REGISTER] + [reg])
        if x:
            return x[0]
        else:
            return False
