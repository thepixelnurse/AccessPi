from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

relay_pins = [17, 27, 22, 5, 6, 13, 19, 26]
GPIO.setmode(GPIO.BCM)

for pin in relay_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def unlock_door(pin):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pin, GPIO.HIGH)

@app.route('/unlock', methods=['POST'])
def unlock():
    door_id = int(request.json['door_id'])
    unlock_door(relay_pins[door_id - 1])
    return "Door unlocked", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)