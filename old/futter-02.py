


from threading import Event
import drivers
from time import sleep
import json
from gpiozero import Button, DigitalOutputDevice, RotaryEncoder

display = drivers.Lcd()
rotor = RotaryEncoder(16, 20, wrap=False, max_steps=5)
rotor.steps = 0
done = Event()
motor = DigitalOutputDevice(18)
feedButton = Button(23)
momentaryButton = Button(24)

with open('settings.json') as f:
  settings = json.load(f)

feeding = False

def onRotateClockwise():
    global settings
    print("rotate clockwise")
    print(settings["foodWeight"])
    if settings["foodWeight"] < 500:
        settings["foodWeight"] += 50
    displayValues()
    saveSettings()

def onRotateCounterClockwise():
    global settings
    print("rotate counter clockwise")
    if settings["foodWeight"] > 50:
        settings["foodWeight"] -= 50
    displayValues()
    saveSettings()

def displayValues():
    print(settings["foodWeight"])
    durationFactor = (settings["foodWeight"] / 50)
    display.lcd_clear()
    display.lcd_display_string("Mahlzeit!", 1)
    display.lcd_display_string("Futterausgabe:", 2)
    display.lcd_display_string(str(round(settings["foodWeight"],2)) + " Gramm (" + str(round(durationFactor * settings["duration_50g"],2)) + 's)', 3)
    if feeding:
        display.lcd_display_string("Fuetterung...",4)
    else:
        display.lcd_display_string("Betriebsbereit.",4)


def feed():
    global feeding
    durationFactor = (settings["foodWeight"] / 50)
    startFeeding()
    print('feeding started')
    sleep(settings["duration_50g"] * durationFactor)
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

def saveSettings():
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=2)


rotor.when_rotated_clockwise = onRotateClockwise
rotor.when_rotated_counter_clockwise = onRotateCounterClockwise

feedButton.when_pressed = feed
momentaryButton.when_pressed = startFeeding
momentaryButton.when_released = stopFeeding

displayValues()



done.wait()
