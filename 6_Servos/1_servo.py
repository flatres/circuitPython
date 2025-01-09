import time
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

print("Servo Motion Detector")

# Mode button setup
button = DigitalInOut(board.GP2)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Servo setup
pwm_servo = pwmio.PWMOut(board.GP28, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(
    pwm_servo, min_pulse=500, max_pulse=2500
)  # tune pulse for specific servo

servo1.angle = 0

def run_motion():
    print("servo 180")
    servo1.angle = 180
    time.sleep(4)

while True:
    if button.value:
        time.sleep(0.8)
        run_motion()
        
    print("servo 0")
    servo1.angle = 0
    
    
#CHALLENGES
    
#1 Add an LED that lights up when motion is detected
#2 Add a buzzer that sounds when motion is detected    
#3 Create a dial that gives a new random number between 1 and 5 when motion is detected
  
