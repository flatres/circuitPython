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

from eng.default import *

#from eng.default import buttons

i2c = busio.I2C(board.GP17, board.GP16)    # Pi Pico RP2040

# Setup
displayio.release_displays()
display_bus = I2CDisplayBus(i2c, device_address=0x3c)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
display.root_group = displayio.Group()

# Draw a splash screen
text = "Loading..."
text_area = label.Label(terminalio.FONT, text=text, x=30, y=32)
display.root_group.append(text_area)

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

switch3U = digitalio.DigitalInOut(board.GP8)
switch3U.direction = digitalio.Direction.INPUT
switch3U.pull = digitalio.Pull.UP

switch3D = digitalio.DigitalInOut(board.GP9)
switch3D.direction = digitalio.Direction.INPUT
switch3D.pull = digitalio.Pull.UP

contStopped = 110

servo0 = servo.Servo(pca.channels[0], min_pulse=400, max_pulse=2400)
servo0.name='Servo 0'
servo0.type = 'cont'
servo0.inc = 40
servo0.delay = 0
servo0.angle = contStopped
servo0.default = contStopped

servo1 = servo.Servo(pca.channels[1], min_pulse=400, max_pulse=2400)
servo1.name='Servo 1'
servo1.type = 'cont'
servo1.inc = 40
servo1.delay = 0
servo1.angle = contStopped
servo1.default = contStopped

servo2 = servo.Servo(pca.channels[2], min_pulse=400, max_pulse=2400)
servo2.name='Servo 2'
servo2.type = 'cont'
servo2.inc = 40
servo2.delay = contStopped
servo2.angle = contStopped


servo3 = servo.Servo(pca.channels[3], min_pulse=400, max_pulse=2400)
servo3.name='Servo 3'
servo3.type = 'cont'
servo3.inc = 40
servo3.delay = contStopped
servo3.angle = contStopped

servo4 = servo.Servo(pca.channels[4], min_pulse=400, max_pulse=2400)
servo4.name='Servo 4'
servo4.type = 'norm'
servo4.inc = 2
servo4.delay = 0
servo4.angle = 0

servo5 = servo.Servo(pca.channels[5], min_pulse=400, max_pulse=2400)
servo5.name='Servo 5'
servo5.type = 'norm'
servo5.inc = 2
servo5.delay = 0
servo5.angle = 0

page = 1

print('running')

def printAngles():
    #clear the display     
    display.root_group = displayio.Group()

    #update time
    text_area = label.Label(terminalio.FONT, text=str(page), x=0, y=12)
    display.root_group.append(text_area)

    text_area = label.Label(terminalio.FONT, text=str(int(servo0.angle)) + ' : ' + str(int(servo1.angle)) + ' : ' + str(int(servo2.angle)), x=0, y=32)
    display.root_group.append(text_area)
    
    text_area = label.Label(terminalio.FONT, text=str(int(servo3.angle)) + ' : ' + str(int(servo4.angle)) + ' : ' + str(int(servo5.angle)), x=0, y=42)
    display.root_group.append(text_area)


def move(servos, switch):
    led.value = True
    time.sleep(0.1)
    
    #printAngle(servo)
    while switch.value == False:
        for s in servos:
            if s[1] == 'up':
                if s[0].type == 'norm':
                    print(s[0].name + ' - u - ' + str(int(s[0].angle)))
                    check = 180 if s[0].inc > 0 else 0
                    if s[0].angle + s[0].inc <= check:
                        s[0].angle = s[0].angle + s[0].inc                        
                elif s[0].type == 'cont':
                    s[0].angle = contStopped + s[0].inc
                
            elif s[1] == 'down':
                print(s[0].name + ' - d - ' + str(int(s[0].angle)))
                check = 0 if s[0].inc > 0 else 180
                if s[0].type == 'norm':
                    if s[0].angle - s[0].inc >= check:
                        s[0].angle = s[0].angle - s[0].inc
                elif s[0].type == 'cont':
                    s[0].angle = contStopped - s[0].inc
                
    for s in servos:
        if s[0].type == 'cont':
            s[0].angle = contStopped
    
    printAngles()
    
 
display.root_group = displayio.Group() 
text = "ready"
#text_area = label.Label(terminalio.FONT, text=text, x=50, y=32)
#display.root_group.append(text_area) 

printAngles()

while True:

    if page == 1:
        if switch0U.value == False:
            button = switch0U
            move([[servo0, 'up']], button)
            
        elif switch0D.value == False:
            button = switch0D
            move([[servo0, 'down']], button)
            
        elif switch1U.value == False:
            button = switch1U
            move([[servo1, 'up']], button)
            
        elif switch1D.value == False:
            button = switch1D
            move([[servo1, 'down']], button)
            
        elif switch2U.value == False:
            button = switch2U
            move([[servo2, 'up']], button)
            
        elif switch2D.value == False:
            button = switch2D
            move([[servo2, 'down']], button)
            
        else:
            led.value = False
            
    if page == 2:
        if switch0U.value == False:
            button = switch0U
            move([[servo3, 'up']], button)
            
        elif switch0D.value == False:
            button = switch0D
            move([[servo3, 'down']], button)
            
        elif switch1U.value == False:
            button = switch1U
            move([[servo4, 'up'], [servo5, 'down']], button)
            
        elif switch1D.value == False:
            button = switch1D
            move([[servo4, 'down'], [servo4, 'up']], button)
            
        elif switch2U.value == False:
            button = switch2U
            move([[servo0, 'up'], [servo1, 'down']], button)
            
        elif switch2D.value == False:
            button = switch2D
            move([[servo0, 'down'], [servo1, 'up']], button)
            
        else:
            led.value = False
        
    #page switching buttons     
    if switch3D.value == False:
        print('page:' + str(page))
        if page == 1:
            page = 2
        elif page == 2:
            page = 1
        printAngles()
        
    elif switch3U.value == False:
        print('something special')
        servo1.angle = servo1.default
        servo0.angle = servo0.default
        printAngles()
    
        
    time.sleep(0.1)
      