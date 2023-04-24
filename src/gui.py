from PyQt6.QtWidgets import QWidget, QPushButton, QLabel
from variables import temperature, room_temperature, heat

import thermostat
import logging

var_temp = 10
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


class Gui(QWidget):
    
    def __init__(self, width, height, title):
        super().__init__()

        self.width = width
        self.height = height
        self.title = title
        self.temperature = temperature
        self.room_temperature = room_temperature
        self.heat = heat
        self.thermostat = thermostat.Thermostat()

        self.temp_thermostat = self.thermostat.get_temperature_threshold()


        self.btn = QPushButton("", self)
        self.btn.setGeometry(180, 140, 150, 150)
        # self.btn.setCheckable(self.heat)
        self.btn.clicked.connect(self.heat_status)

        btn_increment = QPushButton("+", self)
        btn_increment.setGeometry(110,90, 30, 30)
        btn_increment.clicked.connect(self.increment_temperature)

        btn_decrement = QPushButton("-", self)
        btn_decrement.setGeometry(50,90, 30, 30)
        if(self.heat == True):
            self.btn.setStyleSheet("border-radius: 75%; background-color: green")

        else:
            self.btn.setStyleSheet("border-radius: 75%; background-color: red")
        btn_decrement.clicked.connect(self.decrement_temperature)

        set_label = QLabel("Set:", self)
        set_label.move(50,50)
        set_label.setStyleSheet("font-size: 20px")

        test_label = QLabel(f"Test: {self.temp_thermostat}", self)
        test_label.move(100,400)
        test_label.setStyleSheet("font-size: 20px")

        set_label = QLabel("Room:", self)
        set_label.move(350,50)
        set_label.setStyleSheet("font-size: 20px")

        self.room_temperature_label = QLabel(f"{self.temp_thermostat} C", self)
        self.room_temperature_label.move(420, 50)
        self.room_temperature_label.setStyleSheet("font-size: 20px")

        self.temperature_label = QLabel(f"{temperature} C", self)
        self.temperature_label.move(90, 50)
        self.temperature_label.setStyleSheet("font-size: 20px")

        if self.heat == True:
            self.heat_label = QLabel(f"Heat: On", self)
        else:
            self.heat_label = QLabel(f"Heat: Off", self)

        self.heat_label.move(215,300)
        self.heat_label.setStyleSheet("font-size: 20px")


    def build(self):
        self.resize(self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()
    

    def increment_temperature(self):
        logging.debug("increment")
        logging.debug(self.temperature)
        self.temperature += 1
        logging.debug(self.temperature)
        self.temperature_label.setText(f"{self.temperature} C")

    
    def decrement_temperature(self):
        logging.debug("decrement")
        logging.debug(self.temperature)
        self.temperature -= 1
        logging.debug(self.temperature)
        self.temperature_label.setText(f"{self.temperature} C")

    def heat_status(self):
 
        logging.debug(f" it is {self.heat}")

        if self.heat == False:
            logging.debug("entry in False")
            self.btn.setStyleSheet("border-radius: 75%; background-color: green")
            self.heat_label.setText(f"Heat: On")
            self.heat = True
            logging.debug(f"Becomes {self.heat}")

        elif self.heat == True:
            logging.debug("entry in True")
            self.btn.setStyleSheet("border-radius: 75%; background-color: red")

            self.heat_label.setText(f"Heat: Off")
            self.heat = False
            logging.debug(f"Becomes {self.heat}")





