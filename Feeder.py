from pickle import FALSE
from gpiozero import Button, DigitalOutputDevice, RotaryEncoder
from threading import Timer


class Feeder:
    isFeeding = False

    def __init__(self, motorPin, feedButtonPin, momentaryButtonPin):
        self.motor = DigitalOutputDevice(motorPin)
        self.feedButton = Button(feedButtonPin)
        self.momentaryButton = Button(momentaryButtonPin)
        
        self.initButtonEvents()
    
    def initButtonEvents(self):
        self.feedButton.when_pressed = self.feedOnce
        self.momentaryButton.when_pressed = self.startFeeding
        self.momentaryButton.when_released = self.stopFeeding


    def feedOnce(self):
        print('feedOnce')
        self.startFeeding()
        (Timer(2.0, self.stopFeeding)).start()

    def startFeeding(self):
        if not self.isFeeding:
            print('startFeeding')
            self.motor.on()
            self.isFeeding = True

    def stopFeeding(self):
        print('stopFeeding')
        self.motor.off()
        self.isFeeding = False
    

