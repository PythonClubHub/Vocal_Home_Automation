import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

connection = sqlite3.connect('database/data.db')

# create a cursor object
c = connection.cursor()

# execute a query to create a new table
# c.execute('''CREATE TABLE IF NOT EXISTS temp_table
#              (id INTEGER PRIMARY KEY,
#                 temeperature INTEGER,
#                 status INTEGER
#         )''')

#insert data into the table
c.execute("INSERT INTO temp_table (temeperature, status) VALUES (10, 1)")

# retrieve data from the table
# c.execute("SELECT * FROM temperature")
# row = c.fetchall()

# logging.debug(row)

# commit the transaction
connection.commit()

# close the connectionection
connection.close()
