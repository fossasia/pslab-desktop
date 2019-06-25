import math, sys, time, struct

# allows to pack numeric values into byte strings
Byte = struct.Struct("B")  # size 1
ShortInt = struct.Struct("H")  # size 2
Integer = struct.Struct("I")  # size 4

ACKNOWLEDGE = Byte.pack(254)
MAX_SAMPLES = 10000
DATA_SPLITTING = 200

# /*----flash memory----*/
FLASH = Byte.pack(1)
READ_FLASH = Byte.pack(1)
WRITE_FLASH = Byte.pack(2)
WRITE_BULK_FLASH = Byte.pack(3)
READ_BULK_FLASH = Byte.pack(4)

# /*-----ADC------*/
ADC = Byte.pack(2)
CAPTURE_ONE = Byte.pack(1)
CAPTURE_TWO = Byte.pack(2)
CAPTURE_DMASPEED = Byte.pack(3)
CAPTURE_FOUR = Byte.pack(4)
CONFIGURE_TRIGGER = Byte.pack(5)
GET_CAPTURE_STATUS = Byte.pack(6)
GET_CAPTURE_CHANNEL = Byte.pack(7)
SET_PGA_GAIN = Byte.pack(8)
GET_VOLTAGE = Byte.pack(9)
GET_VOLTAGE_SUMMED = Byte.pack(10)
START_ADC_STREAMING = Byte.pack(11)
SELECT_PGA_CHANNEL = Byte.pack(12)
CAPTURE_12BIT = Byte.pack(13)
CAPTURE_MULTIPLE = Byte.pack(14)
SET_HI_CAPTURE = Byte.pack(15)
SET_LO_CAPTURE = Byte.pack(16)

MULTIPOINT_CAPACITANCE = Byte.pack(20)
SET_CAP = Byte.pack(21)
PULSE_TRAIN = Byte.pack(22)

# /*-----SPI--------*/
SPI_HEADER = Byte.pack(3)
START_SPI = Byte.pack(1)
SEND_SPI8 = Byte.pack(2)
SEND_SPI16 = Byte.pack(3)
STOP_SPI = Byte.pack(4)
SET_SPI_PARAMETERS = Byte.pack(5)
SEND_SPI8_BURST = Byte.pack(6)
SEND_SPI16_BURST = Byte.pack(7)
# /*------I2C-------*/
I2C_HEADER = Byte.pack(4)
I2C_START = Byte.pack(1)
I2C_SEND = Byte.pack(2)
I2C_STOP = Byte.pack(3)
I2C_RESTART = Byte.pack(4)
I2C_READ_END = Byte.pack(5)
I2C_READ_MORE = Byte.pack(6)
I2C_WAIT = Byte.pack(7)
I2C_SEND_BURST = Byte.pack(8)
I2C_CONFIG = Byte.pack(9)
I2C_STATUS = Byte.pack(10)
I2C_READ_BULK = Byte.pack(11)
I2C_WRITE_BULK = Byte.pack(12)
I2C_ENABLE_SMBUS = Byte.pack(13)
I2C_INIT = Byte.pack(14)
I2C_PULLDOWN_SCL = Byte.pack(15)
I2C_DISABLE_SMBUS = Byte.pack(16)
I2C_START_SCOPE = Byte.pack(17)

# /*------UART2--------*/
UART_2 = Byte.pack(5)
SEND_BYTE = Byte.pack(1)
SEND_INT = Byte.pack(2)
SEND_ADDRESS = Byte.pack(3)
SET_BAUD = Byte.pack(4)
SET_MODE = Byte.pack(5)
READ_BYTE = Byte.pack(6)
READ_INT = Byte.pack(7)
READ_UART2_STATUS = Byte.pack(8)

# /*-----------DAC--------*/
DAC = Byte.pack(6)
SET_DAC = Byte.pack(1)
SET_CALIBRATED_DAC = Byte.pack(2)

# /*--------WAVEGEN-----*/
WAVEGEN = Byte.pack(7)
SET_WG = Byte.pack(1)
SET_SQR1 = Byte.pack(3)
SET_SQR2 = Byte.pack(4)
SET_SQRS = Byte.pack(5)
TUNE_SINE_OSCILLATOR = Byte.pack(6)
SQR4 = Byte.pack(7)
MAP_REFERENCE = Byte.pack(8)
SET_BOTH_WG = Byte.pack(9)
SET_WAVEFORM_TYPE = Byte.pack(10)
SELECT_FREQ_REGISTER = Byte.pack(11)
DELAY_GENERATOR = Byte.pack(12)
SET_SINE1 = Byte.pack(13)
SET_SINE2 = Byte.pack(14)

LOAD_WAVEFORM1 = Byte.pack(15)
LOAD_WAVEFORM2 = Byte.pack(16)
SQR1_PATTERN = Byte.pack(17)
# /*-----digital outputs----*/
DOUT = Byte.pack(8)
SET_STATE = Byte.pack(1)

# /*-----digital inputs-----*/
DIN = Byte.pack(9)
GET_STATE = Byte.pack(1)
GET_STATES = Byte.pack(2)

ID1 = Byte.pack(0)
ID2 = Byte.pack(1)
ID3 = Byte.pack(2)
ID4 = Byte.pack(3)
LMETER = Byte.pack(4)

# /*------TIMING FUNCTIONS-----*/
TIMING = Byte.pack(10)
GET_TIMING = Byte.pack(1)
GET_PULSE_TIME = Byte.pack(2)
GET_DUTY_CYCLE = Byte.pack(3)
START_ONE_CHAN_LA = Byte.pack(4)
START_TWO_CHAN_LA = Byte.pack(5)
START_FOUR_CHAN_LA = Byte.pack(6)
FETCH_DMA_DATA = Byte.pack(7)
FETCH_INT_DMA_DATA = Byte.pack(8)
FETCH_LONG_DMA_DATA = Byte.pack(9)
GET_LA_PROGRESS = Byte.pack(10)
GET_INITIAL_DIGITAL_STATES = Byte.pack(11)

TIMING_MEASUREMENTS = Byte.pack(12)
INTERVAL_MEASUREMENTS = Byte.pack(13)
CONFIGURE_COMPARATOR = Byte.pack(14)
START_ALTERNATE_ONE_CHAN_LA = Byte.pack(15)
START_THREE_CHAN_LA = Byte.pack(16)
STOP_LA = Byte.pack(17)

# /*--------MISCELLANEOUS------*/
COMMON = Byte.pack(11)

GET_CTMU_VOLTAGE = Byte.pack(1)
GET_CAPACITANCE = Byte.pack(2)
GET_FREQUENCY = Byte.pack(3)
GET_INDUCTANCE = Byte.pack(4)

GET_VERSION = Byte.pack(5)

RETRIEVE_BUFFER = Byte.pack(8)
GET_HIGH_FREQUENCY = Byte.pack(9)
CLEAR_BUFFER = Byte.pack(10)
SET_RGB1 = Byte.pack(11)
READ_PROGRAM_ADDRESS = Byte.pack(12)
WRITE_PROGRAM_ADDRESS = Byte.pack(13)
READ_DATA_ADDRESS = Byte.pack(14)
WRITE_DATA_ADDRESS = Byte.pack(15)

GET_CAP_RANGE = Byte.pack(16)
SET_RGB2 = Byte.pack(17)
READ_LOG = Byte.pack(18)
RESTORE_STANDALONE = Byte.pack(19)
GET_ALTERNATE_HIGH_FREQUENCY = Byte.pack(20)
SET_RGB3 = Byte.pack(22)

START_CTMU = Byte.pack(23)
STOP_CTMU = Byte.pack(24)

START_COUNTING = Byte.pack(25)
FETCH_COUNT = Byte.pack(26)
FILL_BUFFER = Byte.pack(27)

# /*---------- BAUDRATE for main comm channel----*/
SETBAUD = Byte.pack(12)
BAUD9600 = Byte.pack(1)
BAUD14400 = Byte.pack(2)
BAUD19200 = Byte.pack(3)
BAUD28800 = Byte.pack(4)
BAUD38400 = Byte.pack(5)
BAUD57600 = Byte.pack(6)
BAUD115200 = Byte.pack(7)
BAUD230400 = Byte.pack(8)
BAUD1000000 = Byte.pack(9)

# /*-----------NRFL01 radio module----------*/
NRFL01 = Byte.pack(13)
NRF_SETUP = Byte.pack(1)
NRF_RXMODE = Byte.pack(2)
NRF_TXMODE = Byte.pack(3)
NRF_POWER_DOWN = Byte.pack(4)
NRF_RXCHAR = Byte.pack(5)
NRF_TXCHAR = Byte.pack(6)
NRF_HASDATA = Byte.pack(7)
NRF_FLUSH = Byte.pack(8)
NRF_WRITEREG = Byte.pack(9)
NRF_READREG = Byte.pack(10)
NRF_GETSTATUS = Byte.pack(11)
NRF_WRITECOMMAND = Byte.pack(12)
NRF_WRITEPAYLOAD = Byte.pack(13)
NRF_READPAYLOAD = Byte.pack(14)
NRF_WRITEADDRESS = Byte.pack(15)
NRF_TRANSACTION = Byte.pack(16)
NRF_START_TOKEN_MANAGER = Byte.pack(17)
NRF_STOP_TOKEN_MANAGER = Byte.pack(18)
NRF_TOTAL_TOKENS = Byte.pack(19)
NRF_REPORTS = Byte.pack(20)
NRF_WRITE_REPORT = Byte.pack(21)
NRF_DELETE_REPORT_ROW = Byte.pack(22)

NRF_WRITEADDRESSES = Byte.pack(23)

# ---------Non standard IO protocols--------

NONSTANDARD_IO = Byte.pack(14)
HX711_HEADER = Byte.pack(1)
HCSR04_HEADER = Byte.pack(2)
AM2302_HEADER = Byte.pack(3)
TCD1304_HEADER = Byte.pack(4)
STEPPER_MOTOR = Byte.pack(5)

# --------COMMUNICATION PASSTHROUGHS--------
# Data sent to the device is directly routed to output ports such as (SCL, SDA for UART)

PASSTHROUGHS = Byte.pack(15)
PASS_UART = Byte.pack(1)

# /*--------STOP STREAMING------*/
STOP_STREAMING = Byte.pack(253)

# /*------INPUT CAPTURE---------*/
# capture modes
EVERY_SIXTEENTH_RISING_EDGE = Byte.pack(0b101)
EVERY_FOURTH_RISING_EDGE = Byte.pack(0b100)
EVERY_RISING_EDGE = Byte.pack(0b011)
EVERY_FALLING_EDGE = Byte.pack(0b010)
EVERY_EDGE = Byte.pack(0b001)
DISABLED = Byte.pack(0b000)

# /*--------Chip selects-----------*/
CSA1 = Byte.pack(1)
CSA2 = Byte.pack(2)
CSA3 = Byte.pack(3)
CSA4 = Byte.pack(4)
CSA5 = Byte.pack(5)
CS1 = Byte.pack(6)
CS2 = Byte.pack(7)

# resolutions
TEN_BIT = Byte.pack(10)
TWELVE_BIT = Byte.pack(12)


def applySIPrefix(value, unit='', precision=2):
    neg = False
    if value < 0.:
        value *= -1
        neg = True
    elif value == 0.:
        return '0 '  # mantissa & exponnt both 0
    exponent = int(math.log10(value))
    if exponent > 0:
        exponent = (exponent // 3) * 3
    else:
        exponent = (-1 * exponent + 3) // 3 * (-3)

    value *= (10 ** (-exponent))
    if value >= 1000.:
        value /= 1000.0
        exponent += 3
    if neg:
        value *= -1
    exponent = int(exponent)
    PREFIXES = "yzafpnum kMGTPEZY"
    prefix_levels = (len(PREFIXES) - 1) // 2
    si_level = exponent // 3
    if abs(si_level) > prefix_levels:
        raise ValueError("Exponent out range of available prefixes.")
    return '%.*f %s%s' % (precision, value, PREFIXES[si_level + prefix_levels], unit)


'''
def reverse_bits(x):
	return int('{:08b}'.format(x)[::-1], 2)

def InttoString(val):
	return	ShortInt.pack(int(val))

def StringtoInt(string):
	return	ShortInt.unpack(string)[0]

def StringtoLong(string):
	return	Integer.unpack(string)[0]

def getval12(val):
	return val*3.3/4095

def getval10(val):
	return val*3.3/1023


def getL(F,C):
	return 1.0/(C*4*math.pi*math.pi*F*F)

def getF(L,C):
	return 1.0/(2*math.pi*math.sqrt(L*C))

def getLx(f1,f2,f3,Ccal):
	a=(f1/f3)**2
	b=(f1/f2)**2
	c=(2*math.pi*f1)**2
	return (a-1)*(b-1)/(Ccal*c)
	
'''
