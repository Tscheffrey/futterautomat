from gpiozero import Button, DigitalOutputDevice
from signal import pause
from time import sleep


button = Button(17)
motor = DigitalOutputDevice(18)

def on_press():
	print("Motor on")
	motor.on()
	sleep(2.3 * 4)
	print("Motor off")
	motor.off()

button.when_pressed = on_press

pause()
