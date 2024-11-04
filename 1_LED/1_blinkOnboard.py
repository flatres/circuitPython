#LED Blink
import board
import digitalio
import time

#Tell Circuitpython that we want to control the output of the onboard LED Pin
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print('hello world')

while True:
    print('off')
    led.value = False
    time.sleep(1)
    
    led.value = True
    time.sleep(1)
    print('on')
    
    
#TASK 1: Change the 'Hello World' message to "LED Blink"

#TASK 2: Change the speed of the blinking.
# How fast can you go before you can't see it blinking