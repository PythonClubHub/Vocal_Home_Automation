from flask import Flask, jsonify
from flask_cors import CORS
import logging
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def home():
    return jsonify({'message': 'home'})