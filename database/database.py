import sqlite3

connection = sqlite3.connect('data.db')

# create a cursor object
c = connection.cursor()

# execute a query to create a new table
c.execute('''CREATE TABLE IF NOT EXISTS temperature
             (id INTEGER PRIMARY KEY,
                date TEXT,
                hour TEXT, 
                temeperature INTEGER,
                humidity INTEGER
        )''')


c.execute("INSERT INTO temperature (date, hour, temeperature, humidity) VALUES ('13.04.2023','10:03', 20, 5)")

# commit the transaction
connection.commit()

# close the connectionection
connection.close()

