from FeederDisplay import FeederDisplay
from gpiozero import Button, DigitalOutputDevice, RotaryEncoder
from threading import Timer


class Feeder:
    isFeeding = False
    feedingAmount = 50
    maxFeedingAmount = 700
    minFeedingAmount = 50

    def __init__(self, motorPin, feedButtonPin, momentaryButtonPin, rotorPin1, rotorPin2):
        self.motor = DigitalOutputDevice(motorPin)
        self.feedButton = Button(feedButtonPin)
        self.momentaryButton = Button(momentaryButtonPin)
        self.rotor = RotaryEncoder(
            rotorPin1, rotorPin2, wrap=False, max_steps=0)

        self.display = FeederDisplay(self)

        self.display.render()
        self.initButtonEvents()

    def initButtonEvents(self):
        self.feedButton.when_pressed = self.feedOnce
        self.momentaryButton.when_pressed = self.startFeeding
        self.momentaryButton.when_released = self.stopFeeding
        self.rotor.when_rotated_clockwise = self.increaseAmount
        self.rotor.when_rotated_counter_clockwise = self.decreaseAmount

    def feedOnce(self):
        print('feedOnce')
        self.startFeeding()
        (Timer(2.0, self.stopFeeding)).start()

    def startFeeding(self):
        if not self.isFeeding:
            print('startFeeding')
            self.motor.on()
            self.isFeeding = True
            self.display.render()

    def stopFeeding(self):
        print('stopFeeding')
        self.motor.off()
        self.isFeeding = False
        self.display.render()

    def increaseAmount(self):
        if self.feedingAmount < self.maxFeedingAmount:
            self.feedingAmount += 50
            self.display.render()

    def decreaseAmount(self):
        if self.feedingAmount > self.minFeedingAmount:
            self.feedingAmount -= 50
            self.display.render()
