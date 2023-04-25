import sqlite3
from datetime import date
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

today = date.today()
# current_date = today.strftime("%d.%m.%Y")
current_date = '22.04.2023'
logging.debug(f"current date = {current_date}")

# connection = sqlite3.connect('database/data.db')


def average_calling():

# create a cursor object
    # connection = sqlite3.connect('C:/Users/Alex/OneDrive/Documente/PythonClubRepos/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')
    # connection = sqlite3.connect('C:/Users/uif94707/Documents/Python/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')
    connection = sqlite3.connect("C:/Users/uif94707/Documents/Python/Vocal_Home_Automation/Vocal_Home_Automation/src/routes/data.db")


    # create a cursor object
    c = connection.cursor()


    # insert data into the table
    cursor = c.execute("SELECT temperature, humidity FROM temperature WHERE date = ?" , (current_date,))

    suma_temp = 0
    suma_humidity = 0
    i = 0
    j = 0

    logging.debug(cursor)

    for row in cursor:
        logging.debug(row)
        suma_temp += row[0]
        suma_humidity += row[1]
        i = i + 1

    logging.debug(i)
    average_temp = suma_temp / i
    average_temp = round(average_temp, 1)

    average_humidity = suma_humidity / i
    average_humidity = round(average_humidity, 1)

    logging.debug(suma_temp)
    logging.debug(average_temp)

    logging.debug(suma_humidity)
    logging.debug(average_humidity)

    c.execute("INSERT INTO day_average (date, avg_temperature, avg_humidity) VALUES (?, ?, ?)", (current_date, average_temp, average_humidity))
    # c.execute("DELETE FROM day_average WHERE id = 1")

    # commit the transaction
    connection.commit()

    # close the connectionection
    connection.close()


def timer():
    pass

average_calling()
