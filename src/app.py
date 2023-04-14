from flask import Flask, jsonify
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


if __name__ == '__main__':
    app.run(debug=True)