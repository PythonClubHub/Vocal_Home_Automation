

class Thermostat():
    def __init__(self):
        self.threshold_temperature = 19

    def get_temperature_threshold(self):
        return self.threshold_temperature

    def set_temperature_threshold(self, new_threshold_temperature):
        self.threshold_temperature = new_threshold_temperature