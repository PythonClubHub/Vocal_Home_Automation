import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

connection = sqlite3.connect('database/data.db')

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
c.execute("INSERT INTO temperature (date, hour, temeperature, humidity) VALUES ('10.05.2023','13:55', 10, 13)")

# retrieve data from the table
# c.execute("SELECT * FROM temperature")
# row = c.fetchall()

# logging.debug(row)

# commit the transaction
connection.commit()

# close the connectionection
connection.close()
