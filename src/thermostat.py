# import RPi.GPIO as GPIO
import sqlite3
# import sensor

class Thermostat():
    def __init__(self):
        self.relay_pin = 12  # example pin (This pin will be different when app will be finished)
        self.threshold_temperature = 19
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setwarnings(False)
        # GPIO.setup(self.relay_pin,GPIO.OUT)
        # self.sensor = sensor.dht_sensor()


    def get_temperature_threshold(self):
        connection = sqlite3.connect('C:/Users/uif94707/Documents/Python/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')

        # create a cursor object
        c = connection.cursor()


        # insert data into the table
        cursor = c.execute("SELECT temperature FROM temp_table")
        row = c.fetchall()

        self.threshold_temperature = row[0][0]

        return self.threshold_temperature

    def set_temperature_threshold(self, new_threshold_temperature):
        self.threshold_temperature = new_threshold_temperature

    def heating_on(self):
        # GPIO.output(self.relay_pin, GPIO.HIGH)  # if relay_pin is set to HIGH means that the central heating is on
        return "the heating is on"

    def heating_off(self):
        # GPIO.output(self.relay_pin, GPIO.LOW)   # if relay_pin is set to LOW means that the central heating is off
        return "the heating is off"

    def heating_status(self):
        # if GPIO.input(self.relay_pin):
        #     print("Relay is on")
        # else:
        #     print("Relay is off")
        connection = sqlite3.connect('C:/Users/uif94707/Documents/Python/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')

        # create a cursor object
        c = connection.cursor()


        # insert data into the table
        cursor = c.execute("SELECT status FROM temp_table")
        row = c.fetchall()

        heating_status = row[0][0]

        if heating_status == 1:
            return "The heating is ON"
        
        elif heating_status == 0:
            return "The heating status is OFF"

    def compare_temp_with_threshold(self):
        # print(f"Temperature {self.sensor.get_t}, threshold {self.threshold_temperature}")

        connection = sqlite3.connect('C:/Users/uif94707/Documents/Python/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')

        # create a cursor object
        c = connection.cursor()


        # insert data into the table
        cursor = c.execute("SELECT temperature FROM temp_table")
        row = c.fetchall()

        temperature = row[0][0]

        cursor = c.execute("SELECT temperature FROM temperature ORDER BY id DESC LIMIT 1;")

        row = cursor.fetchall()

        last_temp = row[0][0]

        if(temperature < last_temp):
            return f"The heating will STOP ({temperature} < {last_temp})"
        
        elif(temperature > last_temp):
            return f"The heating will START ({temperature} > {last_temp})"

        else:
            return f"The temperature is perfect ({temperature} = {last_temp})"

        # return temperature, last_temp
