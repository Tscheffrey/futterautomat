from threading import Event
from colorzero import Color
from gpiozero import RotaryEncoder
import drivers
from time import sleep

display = drivers.Lcd()
rotor = RotaryEncoder(16, 20, wrap=True, max_steps=10)
rotor.steps = 0
done = Event()

def on_rotate():
	print(rotor.steps)
	display.lcd_clear() 
	display.lcd_display_string("Hi Mika!", 1)
	display.lcd_display_string("Drehgeber:", 2)
	display.lcd_display_string(str(rotor.steps), 3)


rotor.when_rotated = on_rotate

on_rotate()



done.wait()
