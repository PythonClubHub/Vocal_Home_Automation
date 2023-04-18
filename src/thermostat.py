import RPi.GPIO as GPIO

class Thermostat():
    def __init__(self):
        self.relay_pin = 12  # example pin (This pin will be different when app will be finished)
        self.threshold_temperature = 19
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.relay_pin,GPIO.OUT)


    def get_temperature_threshold(self):
        return self.threshold_temperature

    def set_temperature_threshold(self, new_threshold_temperature):
        self.threshold_temperature = new_threshold_temperature

    def heating_on(self):
        GPIO.output(self.relay_pin, GPIO.HIGH)  # if relay_pin is set to HIGH means that the central heating is on

    def heating_off(self):
        GPIO.output(self.relay_pin, GPIO.LOW)   # if relay_pin is set to LOW means that the central heating is off

    def heating_status(self):
        if GPIO.input(self.relay_pin):
            print("Relay is on")
        else:
            print("Relay is off")