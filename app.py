from flask import Flask, redirect, jsonify

from Feeder import *

app = Flask(__name__, static_folder = 'dist', static_url_path = '/app')

f = Feeder(18)

@app.route("/")
def hello_world():
    return redirect('/app/index.html')


@app.route("/api/feed")
def feed():
    f.feedOnce()
    return jsonify({'success': True})