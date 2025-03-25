#LED Blink
import board
import digitalio
import time
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(board.GP17, board.GP16)    # Pi Pico RP2040

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
pca.frequency = 50


servo0 = servo.Servo(pca.channels[0], min_pulse=400, max_pulse=2400)
servo0.name='Servo 0'
servo0.type = 'norm'
servo0.inc = 1
servo0.delay = 0.001
servo0.angle = 90

#Tell Circuitpython that we want to control the output of the onboard LED Pin
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

switch0U = digitalio.DigitalInOut(board.GP2)
switch0U.direction = digitalio.Direction.INPUT
switch0U.pull = digitalio.Pull.UP

switch0D = digitalio.DigitalInOut(board.GP3)
switch0D.direction = digitalio.Direction.INPUT
switch0D.pull = digitalio.Pull.UP


print('running')

inc = 1
delay = 0.001
servo0.inc = 1

servo0.type = 'cont'

def move(servo, switch, direction):
    led.value = True
    time.sleep(0.1)
    while switch.value == False:

        if direction == 'up':
            print('u' + str(int(servo.angle)))
            if servo.angle + servo.inc <= 180:
                servo.angle = servo.angle + servo.inc
                time.sleep(servo.delay)
        elif direction == 'down':
            print('d' + str(int(servo.angle)))
            if servo.angle - servo.inc >= 0:
                servo.angle = servo.angle - servo.inc
                time.sleep(servo.delay)


while True:

    if switch0U.value == False:
        move(servo0, switch0U, 'up')
    elif switch0D.value == False:
        print('d')
        move(servo0, switch0D, 'down')
    else:
        led.value = False
        time.sleep(0.1)
        
      