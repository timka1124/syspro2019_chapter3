import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

while True:
    GPIO.output(14, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(14,GPIO.OUT)
    time.sleep(1)

GPIO.cleanup()
