from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
import sqlite3
from datetime import date

app = Flask(__name__)
CORS(app)


@app.route('/', methods = ['GET'])
def home():
    # return jsonify({'message': 'home'})
    connection = sqlite3.connect('C:/Users/Alex/OneDrive/Documente/PythonClubRepos/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')

    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM day_average
    ''')

    rows = cursor.fetchall()

    connection.close()

    return jsonify(rows)

@app.route('/data', methods = ['GET'])
def data():
    # return jsonify({'message': 'home'})
    connection = sqlite3.connect('C:/Users/Alex/OneDrive/Documente/PythonClubRepos/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')

    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM temp_table
    ''')

    rows = cursor.fetchall()

    connection.close()

    return jsonify(rows)


@app.route('/update_temperature', methods = ['POST'])
def change_temp():
    temperature = request.json.get('temperature')
    connection = sqlite3.connect('C:/Users/Alex/OneDrive/Documente/PythonClubRepos/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')

    cursor = connection.cursor()

    cursor.execute(f'''
        UPDATE temp_table SET temperature = {temperature} WHERE id = 1
    ''')

    connection.commit()
    connection.close()

    return jsonify({'message': 'Temperature updated successfully'})


@app.route('/turn_on', methods = ['POST'])
def turn_on():
    status = request.json.get('on')
    connection = sqlite3.connect('C:/Users/Alex/OneDrive/Documente/PythonClubRepos/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')

    cursor = connection.cursor()

    cursor.execute(f'''
        UPDATE temp_table SET status = {status} WHERE id = 1
    ''')

    connection.commit()
    connection.close()

    return jsonify({'message': 'Turn On successfully'})

@app.route('/turn_off', methods = ['POST'])
def turn_off():
    status = request.json.get('off')
    connection = sqlite3.connect('C:/Users/Alex/OneDrive/Documente/PythonClubRepos/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')

    cursor = connection.cursor()

    cursor.execute(f'''
        UPDATE temp_table SET status = {status} WHERE id = 1
    ''')

    connection.commit()
    connection.close()

    return jsonify({'message': 'Turn On successfully'})



@app.route('/day_data', methods = ['GET'])
def date_temp():
    today = date.today()
    # current_date = today.strftime("%d.%m.%Y")
    current_date = '26.05.2023'
    logging.debug(f"current date = {current_date}")

    connection = sqlite3.connect('C:/Users/Alex/OneDrive/Documente/PythonClubRepos/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')

    cursor = connection.cursor()

    cursor.execute("SELECT date, temperature, humidity FROM temperature WHERE date = ?", (current_date,)
    )

    rows = cursor.fetchall()

    connection.close()
    return jsonify(rows)


@app.route('/week_data', methods = ['GET'])
def week_data():

    connection = sqlite3.connect('C:/Users/Alex/OneDrive/Documente/PythonClubRepos/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')

    cursor = connection.cursor()

    cursor.execute("SELECT avg_temperature, avg_humidity FROM day_average")

    rows = cursor.fetchall()

    connection.close()
    return jsonify(rows)


@app.route('/temperature', methods = ['GET'])
def temp_day():

    connection = sqlite3.connect('C:/Users/Alex/OneDrive/Documente/PythonClubRepos/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')

    cursor = connection.cursor()

    cursor.execute("SELECT date, hour, temperature, humidity FROM temperature")

    rows = cursor.fetchall()

    connection.close()
    return jsonify(rows)


if __name__ == '__main__':
    app.run(debug=True)