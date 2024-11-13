# import libraries
import board, busio, displayio, digitalio, time, terminalio

from i2cdisplaybus import I2CDisplayBus
from adafruit_display_text import label
import adafruit_displayio_ssd1306

import adafruit_rgbled

# Setup
displayio.release_displays()
i2c = busio.I2C(board.GP17, board.GP16)  # uses board.SCL and board.SDA
display_bus = I2CDisplayBus(i2c, device_address=0x3c)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
display.root_group = displayio.Group()

switch1 = digitalio.DigitalInOut(board.GP14)
switch1.direction = digitalio.Direction.INPUT
switch1.pull = digitalio.Pull.UP

switch2 = digitalio.DigitalInOut(board.GP13)
switch2.direction = digitalio.Direction.INPUT
switch2.pull = digitalio.Pull.UP

# Pin the Red LED is connected to
RED = board.GP2
GREEN = board.GP1
BLUE = board.GP0

# Create the RGB LED object
led = adafruit_rgbled.RGBLED(RED, GREEN, BLUE)

# Draw a splash screen
text = "Press Btn"
text_area = label.Label(terminalio.FONT, text=text, x=30, y=32)
display.root_group.append(text_area)
time.sleep(1)

seconds = 10
started = False
finished = False

while True:
    
    if switch1.value == False:
        started = True
        
        if finished == True:
            seconds = 10
            finished = False
        
    if switch2.value == False:
        seconds = 10
        finished = False
        
        #clear the display     
        display.root_group = displayio.Group()

        #update time
        text_area = label.Label(terminalio.FONT, text=str(seconds), x=60, y=32)
        display.root_group.append(text_area)
        time.sleep(0.5)
            
    if started == False:
        led.color = (255, 0, 0)
        
#     flash blue led    
    if finished == True:
        led.color = (0, 0, 255)
        time.sleep(0.2)
        led.color = (0, 0, 0)
        time.sleep(0.2)
        
    if started == True:   
        led.color = (0, 255, 0)
        
        #clear the display     
        display.root_group = displayio.Group()
    
        #update time
        text_area = label.Label(terminalio.FONT, text=str(seconds), x=60, y=32)
        display.root_group.append(text_area)
        
        seconds = seconds - 1
        
        time.sleep(0.5)
        
        if switch1.value == False:
            started = False
            led.color = (255, 0, 0)
            time.sleep(1)
            
        if seconds < 0:
            started = False
            finished = True
            
        time.sleep(0.5)
    

'''CHALLENGES

1. Change the splash screen so that the user is given instructions on how to use the timer 

2. Modify the code so that the timer counts down from 10 seconds

3. Modify the code so that pressing the button again pauses the timer

4. Add a second button that can be used to reset the timer

5. Add an RGB LED that glows red when the timer is stopped,green when it is running 
and flashes blue when it reaches 0



'''


