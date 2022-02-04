from pickle import FALSE
from gpiozero import DigitalOutputDevice
from threading import Timer


class Feeder:
    isFeeding = False

    def __init__(self, motorPin):
        self.motor = DigitalOutputDevice(motorPin)
        print('init Feeder')

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
