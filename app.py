from flask import Flask, redirect, jsonify
from flask_cors import CORS

from Feeder import *

app = Flask(__name__, static_folder = 'dist', static_url_path = '/')
CORS(app)

feeder = Feeder(18, 23, 24, 16, 20)

@app.route("/")
def hello_world():
    return redirect('/index.html')


@app.route("/api/feed-once")
def feedOnce():
    feeder.feedOnce()
    return jsonify({'success': True})

@app.route("/api/start-feeding")
def startFeeding():
    feeder.startFeeding()
    return jsonify({'success': True})

@app.route("/api/stop-feeding")
def stopFeeding():
    feeder.stopFeeding()
    return jsonify({'success': True})