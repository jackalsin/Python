import RPi.GPIO as GPIO
import time
import os

from client import Client

TRIGGER_TIME = 5
JUDGE_TIME = 15

class PirTest(object):

    def __init__(self):
        self.sensor = 4

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor, GPIO.IN, GPIO.PUD_DOWN)
        self.zeroCount = 0
        self.hasSomeone = False

        self.fh = open("currentState.txt", "a")
        self.finalOuput = 0 # no one is zero, 1 is occupied.
        self.fh = open("currentStateFinal.txt", "a")


    def execute(self):
        previous_state = False
        current_state = False
        self.zeroCount = 0
        while True:
            time.sleep(0.1)
            previous_state = current_state
            current_state = GPIO.input(self.sensor)
            # self.fh.write(str(current_state) + " ")
            if current_state == 1:
                self.zeroCount = 0
            else:
                self.zeroCount += 1
                self.zeroCount = min(self.zeroCount, 200)

            if (self.hasSomeone and self.zeroCount > JUDGE_TIME):
                # someone was there but left
                # self.writeFile(self.sensor, self.hasSomeone)
                self.hasSomeone = False
                print "someone left"

            elif (not (self.hasSomeone) and self.zeroCount == 0):
                # no one there someone comes
                # self.writeFile(self.sensor, self.hasSomeone)
                self.hasSomeone = True
                print "someone occupied"

            # print "the self.count = " + str(self.zeroCount)
            if (self.zeroCount > JUDGE_TIME):
                self.writeFile(self.sensor, 0)
            else:
                self.writeFile(self.sensor, 1)

            print "the self.count = " + str(self.zeroCount)


    # write File
    # senserState : boolean: indicate whether isOccupied
    # sensorID : sensor's id
    def writeFile(self, sensorId, sensorState):

        localTime = time.asctime(time.localtime(time.time()))
        content = str(sensorState)+ " " + localTime + " " + str(sensorId) + "\n"

        self.fh.write(str(content) + " ")
        self.fh.flush()




pir = PirTest()
pir.execute()
