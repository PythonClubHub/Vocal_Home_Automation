import sqlite3
from datetime import date
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

today = date.today()
# current_date = today.strftime("%d.%m.%Y")
current_date = '27.05.2023'
logging.debug(f"current date = {current_date}")

connection = sqlite3.connect('database/data.db')


def average_calling():

# create a cursor object
    connection = sqlite3.connect('C:/Users/Alex/OneDrive/Documente/PythonClubRepos/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')

    # create a cursor object
    c = connection.cursor()


    # insert data into the table
    cursor = c.execute("SELECT temperature FROM temperature WHERE date = ?" , (current_date,))

    suma = 0
    i = 0

    for row in cursor:
        logging.debug(row)
        suma += row[0]
        i = i + 1

    average = suma / i
    average = round(average, 1)

    logging.debug(suma)
    logging.debug(average)

    c.execute("INSERT INTO day_average (date, avg_temperature, avg_humidity) VALUES (?, ?, ?)", (current_date, average, 67))
    # c.execute("DELETE FROM day_average WHERE id = 1")

    # commit the transaction
    connection.commit()

    # close the connectionection
    connection.close()


def timer():
    pass

average_calling()
