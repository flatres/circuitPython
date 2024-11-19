import board
import digitalio
import pwmio

# Setup digital input for PIR sensor:
pir = digitalio.DigitalInOut(board.GP16)
pir.direction = digitalio.Direction.INPUT

buzzer = pwmio.PWMOut(board.GP14, variable_frequency=True)
OFF = 0
ON = 2**15 #Sets the Duty Cycle

# Main loop that will run forever:
old_value = pir.value
while True:
    pir_value = pir.value
    if pir_value == True:
        # PIR is detecting movement! Turn on Buzzer.
        buzzer.frequency = 440
        buzzer.duty_cycle = ON
        
        
        # Check if this is the first time movement was
        # detected and print a message!
        if not old_value:
            print('Motion detected!')
    else:
        # PIR is not detecting movement. Turn off Buzzer.
        buzzer.duty_cycle = OFF
        # Again check if this is the first time movement
        # stopped and print a message.
        if old_value:
            print('Motion ended!')
            
    old_value = pir_value
    
'''CHALLENGES:
1. Can you turn on a red led when motion is detected

2. Can you get the buzzer to alternate between two different frequencies

'''