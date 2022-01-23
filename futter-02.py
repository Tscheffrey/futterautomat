
from threading import Event
from colorzero import Color
from gpiozero import RotaryEncoder
import drivers
from time import sleep
from gpiozero import Button, DigitalOutputDevice

display = drivers.Lcd()
rotor = RotaryEncoder(16, 20, wrap=False, max_steps=5)
rotor.steps = 0
done = Event()
motor = DigitalOutputDevice(18)
fullButton = Button(23)
holdButton = Button(24)

weight = 50
duration_50g = 2.25
feeding = False

def onRotateClockwise():
    global weight
    print("rotate clockwise")
    print(weight)
    if weight < 500:
        weight += 50
    displayValues()

def onRotateCounterClockwise():
    global weight
    print("rotate counter clockwise")
    if weight > 50:
        weight -= 50
    displayValues()

def displayValues():
    print(weight)
    durationFactor = (weight / 50)
    display.lcd_clear()
    display.lcd_display_string("Mahlzeit!", 1)
    display.lcd_display_string("Futterausgabe:", 2)
    display.lcd_display_string(str(round(weight,2)) + " Gramm (" + str(round(durationFactor * duration_50g,2)) + 's)', 3)
    if feeding:
        display.lcd_display_string("Fuetterung...",4)
    else:
        display.lcd_display_string("Betriebsbereit.",4)


def feed():
    global feeding
    durationFactor = (weight / 50)
    startFeeding()
    print('feeding started')
    sleep(duration_50g * durationFactor)
    stopFeeding()
    print('feeding stopped')

def startFeeding():
    global feeding
    motor.on()
    feeding = True
    displayValues()
    print('feeding started')

def stopFeeding():
    global feeding
    motor.off()
    feeding = False
    displayValues()
    print('feeding stopped')


rotor.when_rotated_clockwise = onRotateClockwise
rotor.when_rotated_counter_clockwise = onRotateCounterClockwise

fullButton.when_pressed = feed
holdButton.when_pressed = startFeeding
holdButton.when_released = stopFeeding

displayValues()



done.wait()
