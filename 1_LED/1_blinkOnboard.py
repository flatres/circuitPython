#LED Blink
import board
import digitalio
import time

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