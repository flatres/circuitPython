#LED Blink
import board
import digitalio
import time
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import displayio, terminalio

from i2cdisplaybus import I2CDisplayBus
from adafruit_display_text import label
import adafruit_displayio_ssd1306

i2c = busio.I2C(board.GP17, board.GP16)    # Pi Pico RP2040

# Setup
#displayio.release_displays()
#display_bus = I2CDisplayBus(i2c, device_address=0x3c)
#display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
#display.root_group = displayio.Group()

# Draw a splash screen
#text = "Loading..."
#text_area = label.Label(terminalio.FONT, text=text, x=30, y=32)
#display.root_group.append(text_area)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
pca.frequency = 50

#Tell Circuitpython that we want to control the output of the onboard LED Pin
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

switch0U = digitalio.DigitalInOut(board.GP2)
switch0U.direction = digitalio.Direction.INPUT
switch0U.pull = digitalio.Pull.UP

switch0D = digitalio.DigitalInOut(board.GP3)
switch0D.direction = digitalio.Direction.INPUT
switch0D.pull = digitalio.Pull.UP

switch1U = digitalio.DigitalInOut(board.GP4)
switch1U.direction = digitalio.Direction.INPUT
switch1U.pull = digitalio.Pull.UP

switch1D = digitalio.DigitalInOut(board.GP5)
switch1D.direction = digitalio.Direction.INPUT
switch1D.pull = digitalio.Pull.UP

switch2U = digitalio.DigitalInOut(board.GP6)
switch2U.direction = digitalio.Direction.INPUT
switch2U.pull = digitalio.Pull.UP

switch2D = digitalio.DigitalInOut(board.GP7)
switch2D.direction = digitalio.Direction.INPUT
switch2D.pull = digitalio.Pull.UP

contStopped = 110

servo0 = servo.Servo(pca.channels[0], min_pulse=400, max_pulse=2400)
servo0.name='Servo 0'
servo0.type = 'norm'
servo0.inc = 2
servo0.delay = 0
servo0.angle = 90

servo1 = servo.Servo(pca.channels[1], min_pulse=400, max_pulse=2400)
servo1.name='Servo 1'
servo1.type = 'norm'
servo1.inc = 2
servo1.delay = 0
servo1.angle = 90

servo2 = servo.Servo(pca.channels[2], min_pulse=400, max_pulse=2400)
servo2.name='Servo 2'
servo2.type = 'cont'
servo2.inc = 30
servo2.delay = 0
servo2.angle = contStopped

print('running')

def printAngle(servo):
    #clear the display     
    display.root_group = displayio.Group()

    #update time
    text_area = label.Label(terminalio.FONT, text=servo.name, x=0, y=12)
    display.root_group.append(text_area)

    text_area = label.Label(terminalio.FONT, text='Angle: ' + str(int(servo.angle)), x=0, y=32)
    display.root_group.append(text_area)


def move(servo, switch, direction):
    led.value = True
    time.sleep(0.1)
    #printAngle(servo)
    while switch.value == False:
        if direction == 'up':
            if servo.type == 'norm':
                print(servo.name + ' - u - ' + str(int(servo.angle)))
                if servo.angle + servo.inc <= 180:
                    servo.angle = servo.angle + servo.inc
                    time.sleep(servo.delay)
            elif servo.type == 'cont':
                servo.angle = contStopped + servo.inc
                
        elif direction == 'down':
            print(servo.name + ' - d - ' + str(int(servo.angle)))
            if servo.type == 'norm':
                if servo.angle - servo.inc >= 0:
                    servo.angle = servo.angle - servo.inc
                    time.sleep(servo.delay)
            elif servo.type == 'cont':
                servo.angle = contStopped - servo.inc
                
    if servo.type == 'cont':
        servo.angle = contStopped
                
    #printAngle(servo)
 
#display.root_group = displayio.Group() 
#text = "ready"
#text_area = label.Label(terminalio.FONT, text=text, x=50, y=32)
#display.root_group.append(text_area) 

while True:

    if switch0U.value == False:
        move(servo0, switch0U, 'up')
    elif switch0D.value == False:
        move(servo0, switch0D, 'down')
    elif switch1U.value == False:
        move(servo1, switch1U, 'up')
    elif switch1D.value == False:
        move(servo1, switch1D, 'down')
    elif switch2U.value == False:
        move(servo2, switch2U, 'up')
    elif switch2D.value == False:
        move(servo2, switch2D, 'down')
    else:
        led.value = False
        time.sleep(0.1)
        
      