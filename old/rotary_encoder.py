from threading import Event
from colorzero import Color
from gpiozero import RotaryEncoder

rotor = RotaryEncoder(16, 20, wrap=True, max_steps=10)
rotor.steps = 0
done = Event()

def on_rotate():
	print(rotor.steps)


rotor.when_rotated = on_rotate



done.wait()
