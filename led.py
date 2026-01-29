import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
# ON LED
GPIO.output(18, GPIO.HIGH)
time.sleep(1)
# OFF LED
GPIO.output(18, GPIO.LOW)
GPIO.cleanup()
