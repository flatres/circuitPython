import time
import board
import digitalio

import adafruit_rgbled

# Pin the Red LED is connected to
RED = board.GP2
GREEN = board.GP1
BLUE = board.GP0

# Create the RGB LED object
led = adafruit_rgbled.RGBLED(RED, GREEN, BLUE)

switch = digitalio.DigitalInOut(board.GP17)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

while True:
  led.color = (255, 0, 0)
  if switch.value == False:
      led.color = (0, 255, 0)
      #time.sleep(0.1)

# task 1: add a 0.2 second delay after the color
# changes to green. What happens?

# task 2: Modify your code to flash between blue and
# green when the button is pressed.

# task 3: Add a second button to turn the light white when pressed
      