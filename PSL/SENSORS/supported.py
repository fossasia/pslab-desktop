import inspect

from PSL.SENSORS import HMC5883L
from PSL.SENSORS import MPU6050
from PSL.SENSORS import MLX90614
from PSL.SENSORS import BMP180
from PSL.SENSORS import TSL2561
from PSL.SENSORS import SHT21
from PSL.SENSORS import BH1750
from PSL.SENSORS import SSD1306

supported = {
    0x68: MPU6050,  # 3-axis gyro,3-axis accel,temperature
    0x1E: HMC5883L,  # 3-axis magnetometer
    0x5A: MLX90614,  # Passive IR temperature sensor
    0x77: BMP180,  # Pressure, Temperature, altitude
    0x39: TSL2561,  # Luminosity
    0x40: SHT21,  # Temperature, Humidity
    0x23: BH1750,  # Luminosity
    # 0x3C:SSD1306,    #OLED display
}

# auto generated map of names to classes
nameMap = {}
for a in supported:
    nameMap[supported[a].__name__.split('.')[-1]] = (supported[a])
