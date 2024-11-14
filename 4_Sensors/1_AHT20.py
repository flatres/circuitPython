#import libraries
import time
import board, busio
import adafruit_ahtx0

# Setup
i2c = busio.I2C(board.GP13, board.GP12) #SCL, SDA
sensor = adafruit_ahtx0.AHTx0(i2c)

#Loop
while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)