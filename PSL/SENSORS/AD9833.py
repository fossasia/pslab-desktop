import sys


class AD9833:
    if sys.version.major == 3:
        DDS_MAX_FREQ = 0xFFFFFFF - 1  # 24 bit resolution
    else:
        DDS_MAX_FREQ = eval("0xFFFFFFFL-1")  # 24 bit resolution
    # control bytes
    DDS_B28 = 13
    DDS_HLB = 12
    DDS_FSELECT = 11
    DDS_PSELECT = 10
    DDS_RESET = 8
    DDS_SLEEP1 = 7
    DDS_SLEEP12 = 6
    DDS_OPBITEN = 5
    DDS_DIV2 = 3
    DDS_MODE = 1

    DDS_FSYNC = 9

    DDS_SINE = (0)
    DDS_TRIANGLE = (1 << DDS_MODE)
    DDS_SQUARE = (1 << DDS_OPBITEN)
    DDS_RESERVED = (1 << DDS_OPBITEN) | (1 << DDS_MODE)
    clockScaler = 4  # 8MHz

    def __init__(self, I=None):
        self.CS = 9
        if I:
            self.I = I
        else:
            from PSL import sciencelab
            self.I = sciencelab.connect()
        self.I.SPI.set_parameters(2, 2, 1, 1, 0)
        self.I.map_reference_clock(self.clockScaler, 'WAVEGEN')
        print('clock set to ', self.I.DDS_CLOCK)

        self.waveform_mode = self.DDS_TRIANGLE;
        self.write(1 << self.DDS_RESET)
        self.write((1 << self.DDS_B28) | self.waveform_mode)  # finished loading data
        self.active_channel = 0
        self.frequency = 1000

    def write(self, con):
        self.I.SPI.start(self.CS)
        self.I.SPI.send16(con)
        self.I.SPI.stop(self.CS)

    def set_frequency(self, freq, register=0, **args):
        self.active_channel = register
        self.frequency = freq

        freq_setting = int(round(freq * self.DDS_MAX_FREQ / self.I.DDS_CLOCK))
        modebits = (1 << self.DDS_B28) | self.waveform_mode
        if register:
            modebits |= (1 << self.DDS_FSELECT)
            regsel = 0x8000
        else:
            regsel = 0x4000

        self.write((1 << self.DDS_RESET) | modebits)  # Ready to load DATA
        self.write((regsel | (freq_setting & 0x3FFF)) & 0xFFFF)  # LSB
        self.write((regsel | ((freq_setting >> 14) & 0x3FFF)) & 0xFFFF)  # MSB
        phase = args.get('phase', 0)
        self.write(0xc000 | phase)  # Phase
        self.write(modebits)  # finished loading data

    def set_voltage(self, v):
        self.waveform_mode = self.DDS_TRIANGLE
        self.set_frequency(0, 0, phase=v)  # 0xfff*v/.6)

    def select_frequency_register(self, register):
        self.active_channel = register
        modebits = self.waveform_mode
        if register:    modebits |= (1 << self.DDS_FSELECT)
        self.write(modebits)

    def set_waveform_mode(self, mode):
        self.waveform_mode = mode
        modebits = mode
        if self.active_channel:    modebits |= (1 << self.DDS_FSELECT)
        self.write(modebits)


if __name__ == "__main__":
    from PSL import sciencelab

    I = sciencelab.connect()
    A = AD9833(I=I)
    A.set_waveform_mode(A.DDS_SINE)
    A.set_frequency(3600, 0)
    A.set_frequency(3600, 1)
