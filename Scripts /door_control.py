import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
relay_pins = [17, 27, 22, 5, 6, 13, 19, 26]

for pin in relay_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def unlock_door(relay_pin):
    GPIO.output(relay_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(relay_pin, GPIO.HIGH)

GPIO.cleanup()