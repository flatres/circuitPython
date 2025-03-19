import time
import board
import busio
import keyboard
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

# Initialize I2C and PCA9685
i2c = busio.I2C(board.GP1, board.GP0)  # Pi Pico RP2040
pca = PCA9685(i2c)
pca.frequency = 50

# Initialize servos
servos = {
    'q': servo.Servo(pca.channels[0], min_pulse=400, max_pulse=2400),
    'w': servo.Servo(pca.channels[1], min_pulse=400, max_pulse=2400),
    'e': servo.Servo(pca.channels[2], min_pulse=400, max_pulse=2400),
    'r': servo.Servo(pca.channels[3], min_pulse=400, max_pulse=2400),
    't': servo.Servo(pca.channels[4], min_pulse=400, max_pulse=2400),
}

# Dictionary to store current angles
servo_angles = {key: 90 for key in servos}  # Start all servos at 90 degrees

def move_servos():
    """Continuously check for key presses and move servos accordingly."""
    while True:
        moved = False
        for key, servo in servos.items():
            if keyboard.is_pressed(key):  # Move servo up
                if servo_angles[key] < 180:
                    servo_angles[key] += 2
                    servo.angle = servo_angles[key]
                    moved = True

            if keyboard.is_pressed(key.lower()):  # Move servo down
                if servo_angles[key] > 0:
                    servo_angles[key] -= 2
                    servo.angle = servo_angles[key]
                    moved = True
        
        if moved:
            time.sleep(0.05)  # Delay to control movement speed

try:
    print("Use keys Q, W, E, R, T to move servos up and q, w, e, r, t to move them down.")
    move_servos()

except KeyboardInterrupt:
    print("\nExiting...")
    pca.deinit()
