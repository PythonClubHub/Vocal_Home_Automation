import Adafruit_DHT



class dht_sensor:
    def __init__(self, temp, humid):
        self.temp = temp
        self.humid = humid

dht_sensor22 = Adafruit_DHT.DHT22

dht_pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor22, dht_pin)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retreive data from humidity sensor")