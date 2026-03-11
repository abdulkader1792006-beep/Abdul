import RPi.GPIO as GPIO
import time

# Motor GPIO pins
IN1 = 17
IN2 = 18
IN3 = 22
IN4 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

def move_forward():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def stop_robot():
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)

try:
    print("Robot moving forward...")
    move_forward()
    time.sleep(5)

    print("Robot stopped.")
    stop_robot()

finally:
    GPIO.cleanup()
