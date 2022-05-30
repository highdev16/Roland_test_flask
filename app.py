import os
from flask import Flask, request, jsonify, render_template
from firebase_admin import credentials, firestore, initialize_app
import time

app=Flask(__name__,template_folder='template')


cred = credentials.Certificate('firebase.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')

@app.route("/request", methods=['POST'])
def process_request():
    timestr = time.strftime('%Y_%H_%M_%S')
    value = request.json['value']
    todo_ref.document(timestr).set(request.json)
    
    return jsonify({"success": True}), 200

@app.route("/", methods=['GET'])
def home(): 
    return render_template('index.html')
