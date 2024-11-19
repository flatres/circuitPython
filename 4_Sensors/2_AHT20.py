#import libraries
import time
import board, busio
import adafruit_ahtx0

# Setup
i2c = busio.I2C(board.GP17, board.GP16) #SCL, SDA
sensor = adafruit_ahtx0.AHTx0(i2c)

#Loop
while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)
    
'''
Challenge: Can you turn the temperature sensor into a touch sensor that
turns on an led when you put your finger on it?

'''