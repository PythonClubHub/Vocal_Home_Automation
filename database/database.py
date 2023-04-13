import sqlite3

connection = sqlite3.connect('data.db')

# create a cursor object
c = connection.cursor()

# execute a query to create a new table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# commit the transaction
connection.commit()

# close the connectionection
connection.close()

