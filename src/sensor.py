import Adafruit_DHT



class dht_sensor:
    def __init__(self):
        self.dht_sensor22 = Adafruit_DHT.DHT22
        self.dht_pin = 21

    def get_t(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.dht_sensor22, self.dht_pin)
        if humidity is not None and temperature is not None:
            return str(round(temperature, 2))
        else:
            print("Failed to retreive data from temperature sensor")

    def get_h(self):
        humidity, temperature= Adafruit_DHT.read_retry(self.dht_sensor22, self.dht_pin)
        if humidity is not None and temperature is not None:
            return int(round(humidity, 2))
        else:
            print("Failed to retreive data from humidity sensor")