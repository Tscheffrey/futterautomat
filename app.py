from flask import Flask, redirect, jsonify
from gpiozero import DigitalOutputDevice
from time import sleep
from threading import Timer

app = Flask(__name__, static_folder = 'dist', static_url_path = '/app')

motor = DigitalOutputDevice(18)

@app.route("/")
def hello_world():
    return redirect('/app/index.html')


@app.route("/api/feed")
def feed():
    print("Motor on")
    motor.on()
    (Timer(2.0, motor.off)).start()
    return jsonify({'success': True})