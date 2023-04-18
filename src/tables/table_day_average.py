import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

connection = sqlite3.connect('database/data.db')

# create a cursor object
c = connection.cursor()

# execute a query to create a new table
# c.execute('''CREATE TABLE IF NOT EXISTS average_data
#              (id INTEGER PRIMARY KEY,
#                 date TEXT,
#                 avg_temeperature INTEGER,
#                 avg_humidity INTEGER
#         )''')

#insert data into the table
# c.execute("INSERT INTO day_average (date, avg_temeperature, avg_humidity) VALUES ('17.04.2023', 20, 50)")
# c.execute(("DELETE FROM day_average"))
c.execute("DELETE FROM day_average WHERE id = 4")

# retrieve data from the table
# c.execute("SELECT * FROM temperature")
# row = c.fetchall()

# logging.debug(row)

# commit the transaction
connection.commit()

# close the connectionection
connection.close()