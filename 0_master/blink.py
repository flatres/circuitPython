import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP1)
led.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP2)
led2.direction = digitalio.Direction.OUTPUT

print('hello world')

while True:
    led.value = False
    led2.value = True
    time.sleep(1)
    
    led.value = True
    led2.value = False
    time.sleep(1)
