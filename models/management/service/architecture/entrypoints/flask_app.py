"""
    Flask app 

    - Entrypoints are the places we drive our application from. 
    - In the official ports and adapters terminology, these are adapters too, 
    and are referred to as primary, driving, or outward-facing adapters. 

    export FLASK_APP=flask_app.py  

    export FLASK_APP=entrypoints/flask_app.py  
    export FLASK_ENV=development
"""
#from flask import Flask, jsonify, request
#from sqlalchemy import create_engine 
#from sqlalchemy.orm import sessionmaker 
#from datetime import datetime
from flask import Flask
app = Flask(__name__)

# ------------------------------------ Root ------------------------------------------
@app.route('/')
def index():
    print('*** root')
    return 'Hello, from ARCHITECTURE Flask API !', 201

@app.route('/hello')
def hello():
    print('*** hello')
    return 'Hello world !'
