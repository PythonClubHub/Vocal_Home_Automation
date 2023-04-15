from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
import sqlite3

app = Flask(__name__)
CORS(app)


@app.route('/', methods = ['GET'])
def home():
    # return jsonify({'message': 'home'})
    connection = sqlite3.connect('C:/Users/Alex/OneDrive/Documente/PythonClubRepos/Vocal_Home_Automation/Vocal_Home_Automation/database/data.db')

    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM temperature
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


if __name__ == '__main__':
    app.run(debug=True)