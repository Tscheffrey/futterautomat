from flask import Flask, redirect, jsonify

from Feeder import *

app = Flask(__name__, static_folder = 'dist', static_url_path = '/app')

f = Feeder(18)

@app.route("/")
def hello_world():
    return redirect('/app/index.html')


@app.route("/api/feed-once")
def feedOnce():
    f.feedOnce()
    return jsonify({'success': True})

@app.route("/api/start-feeding")
def startFeeding():
    f.startFeeding()
    return jsonify({'success': True})

@app.route("/api/stop-feeding")
def stopFeeding():
    f.stopFeeding()
    return jsonify({'success': True})