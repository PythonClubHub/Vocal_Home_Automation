from PyQt6.QtWidgets import QWidget, QPushButton, QLabel
from variables import temperature, room_temperature
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

        btn = QPushButton("", self)
        btn.setGeometry(160, 140, 150, 150)
        btn.setStyleSheet("border-radius: 75%; background-color: red")
        # btn.clicked.connect(self.test)

        btn_increment = QPushButton("+", self)
        btn_increment.setGeometry(110,90, 30, 30)
        btn_increment.clicked.connect(self.increment_temperature)

        btn_decrement = QPushButton("-", self)
        btn_decrement.setGeometry(50,90, 30, 30)
        btn_decrement.clicked.connect(self.decrement_temperature)

        set_label = QLabel("Set:", self)
        set_label.move(50,50)
        set_label.setStyleSheet("font-size: 20px")


        set_label = QLabel("Room:", self)
        set_label.move(350,50)
        set_label.setStyleSheet("font-size: 20px")

        self.room_temperature_label = QLabel(f"{room_temperature} C", self)
        self.room_temperature_label.move(420, 50)
        self.room_temperature_label.setStyleSheet("font-size: 20px")

        self.temperature_label = QLabel(f"{temperature} C", self)
        self.temperature_label.move(90, 50)
        self.temperature_label.setStyleSheet("font-size: 20px")

        heat_label = QLabel("Heat:", self)
        heat_label.move(200,300)
        heat_label.setStyleSheet("font-size: 20px")


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


    # def print(self, temp):
    #     self.room_temperature_label.setText(f"{temp} C")



