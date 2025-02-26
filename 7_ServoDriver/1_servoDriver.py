import time
import board
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(board.GP1, board.GP0)    # Pi Pico RP2040

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
pca.frequency = 50


servo1 = servo.Servo(pca.channels[0], min_pulse=400, max_pulse=2400)
servo2 = servo.Servo(pca.channels[1], min_pulse=400, max_pulse=2400)
servo3 = servo.Servo(pca.channels[2], min_pulse=400, max_pulse=2400)
servo4 = servo.Servo(pca.channels[3], min_pulse=400, max_pulse=2400)

delay = 0.003

# We sleep in the loops to give the servo time to move into position.
for i in range(180):
    servo1.angle = i
    servo2.angle = i
    servo3.angle = i
    servo4.angle = i
    time.sleep(delat)
for i in range(180):
    servo1.angle = 180 - i
    servo2.angle = 180 - i
    servo3.angle = 180 - i
    servo4.angle = 180 - i
    time.sleep(delay)

pca.deinit()