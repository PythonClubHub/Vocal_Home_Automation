import Adafruit_DHT



class dht_sensor:
    def __init__(self, temp, humid):
        self.temp = temp
        self.humid = humid
        self.dht_sensor22 = Adafruit_DHT.DHT22
        self.dht_pin = 4

    def get_t(self):
        temperature = Adafruit_DHT.read_retry(self.dht_sensor22, self.dht_pin)
        if temperature is not None:
            return int(round(temperature, 2))
        else:
            print("Failed to retreive data from humidity sensor")

    def get_h(self):
        humidity= Adafruit_DHT.read_retry(self.dht_sensor22, self.dht_pin)
        if humidity is not None:
            return int(round(humidity, 2))
        else:
            print("Failed to retreive data from humidity sensor")