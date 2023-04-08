# Home automation with vocal assistent

Home automation developed mainly in Python that runs on an Raspberry Pi (4).
The project implements the possibility to interact with the home automation either via a GUI or a Vocal assistent,
The main objective is to set the desired home temperature and to control the heating system.


**Apart from these functionalities, we managed to add extra ones that helps the user.**
Aditionaly the vocal assistent can return the temperature outside and the weater status.

# Hardware parts
- Raspberry Pi 4
- Charger
- uSDcard
- HDMI Cable
- temprature & humidity sesnor
- LED 
- 7" touch screen

# Set UP
Step 1: Download Raspberry PI Imager [link](https://www.raspberrypi.com/software/)

Step 2: In the Linux terminal write:
```
sudo apt-get update
```
```
sudo apt-get upgrade
```
Step 3: Remote access:
```
sudo raspi-config 
```
![Screenshot 2023-03-27 at 04 41 55](https://user-images.githubusercontent.com/115079881/227820929-e64c5a04-561b-4853-9da8-b7078e417be3.png)

![Screenshot 2023-03-27 at 04 42 47](https://user-images.githubusercontent.com/115079881/227821017-244e9e4a-1712-4588-87bf-128046b04ec5.png)

Step 4: Reboot:
```
sudo reboot
```
# Install needed components:
- Git
```
sudo apt-get install git
```
# Install python library dependensies:
```
pip3 install RPi.GPIO
pip3 insatll PyQt6
```
