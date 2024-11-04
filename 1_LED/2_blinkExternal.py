import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP1)
led.direction = digitalio.Direction.OUTPUT

print('hello world')

while True:
    print('on')
    led.value = False
    time.sleep(1)
    
    print('off')
    led.value = True
    time.sleep(1)

#TASK: Modify your circuit and code to blink a second LED
# so that when one is off, the other is on