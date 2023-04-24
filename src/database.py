import sqlite3
import logging
from datetime import datetime, date
import random
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

def insert_data():

    # get a random temperature and humidity --------------
    random_temp = random.randint(0, 40)
    logging.debug(f"random temp = {random_temp}")

    random_humidity = random.randint(50, 100)
    logging.debug(f"random humidity = {random_humidity}")

    # get a random time and date ------------------------------
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    logging.debug(f"current time = {current_time}")

    today = date.today()
    # current_date = today.strftime("%d.%m.%Y")
    current_date = '28.05.2023'
    logging.debug(f"current date = {current_date}")

    # connection = sqlite3.connect('C:/Users/Alex/OneDrive/Documente/PythonClubRepos/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')
    # connection = sqlite3.connect('C:/Users/uif94707/Documents/Python/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')
<<<<<<< HEAD:src/tables/database.py
    connection = sqlite3.connect('database/data.db')
=======
    connection = sqlite3.connect("data.db")

>>>>>>> 2895d137364809a282918e70c64b907ce44d585b:src/routes/database.py

    # create a cursor object
    c = connection.cursor()

    # execute a query to create a new table
    # c.execute('''CREATE TABLE IF NOT EXISTS temperature
    #              (id INTEGER PRIMARY KEY,
    #                 date TEXT,
    #                 hour TEXT, 
    #                 temeperature INTEGER,
    #                 humidity INTEGER
    #         )''')

    #insert data into the table
    c.execute("INSERT INTO temperature (date, hour, temperature, humidity) VALUES (?, ? , ?, ?)", (current_date, current_time, random_temp, random_humidity))

    # c.execute("DELETE FROM temperature WHERE id >= 18 AND id <= 266")
    # c.execute("DELETE FROM temperature")
    # retrieve data from the table
    # c.execute("SELECT * FROM temperature")
    # row = c.fetchall()

    # logging.debug(row)

    # commit the transaction
    connection.commit()

    # close the connectionection
    connection.close()


def timer_insert():
    while True:
        insert_data()
        time.sleep(2)

timer_insert()
