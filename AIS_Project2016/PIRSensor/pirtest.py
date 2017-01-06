import RPi.GPIO as GPIO
import time
import os

from client import Client

TRIGGER_TIME = 5
JUDGE_TIME = 150

class PirTest(object):

    def __init__(self):
        self.sensor = 4

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor, GPIO.IN, GPIO.PUD_DOWN)
        self.zeroCount = 0
        self.hasSomeone = False
        self.client = Client();

        self.fh = open("currentState.txt", "a")
        self.finalOuput = 0 # no one is zero, 1 is occupied.

    def execute(self):
        previous_state = False
        current_state = False
        self.zeroCount = 0
        self.oneCount = 0
        while True:
            time.sleep(0.1)
            previous_state = current_state
            current_state = GPIO.input(self.sensor)
            # self.fh.write(str(current_state) + " ")
            if current_state == 1:
                self.zeroCount = 0
                self.oneCount += 1
                self.oneCount = min(self.oneCount, 10)
            else:
                self.oneCount = 0;
                self.zeroCount += 1
                self.zeroCount = min(self.zeroCount, 200)
            if (self.hasSomeone and self.zeroCount > JUDGE_TIME):
                # someone was there but left
                self.writeFile(self.sensor, self.hasSomeone)
                self.hasSomeone = False
                self.client.msg_send_to_sever("Sending from Pir:someone left")
                print "someone left"

            elif (not (self.hasSomeone) and self.oneCount > 7):
                # no one there someone comes
                self.writeFile(self.sensor, self.hasSomeone)
                self.hasSomeone = True
                self.client.msg_send_to_sever("Sending from Pir:someone occupied")
                print "someone occupied"

            print "the self.count = " + str(self.zeroCount) + " " + str(self.oneCount)


            # if current_state != previous_state:
            #     new_state = "HIGH" if current_state else "LOW"
            #     s = "GPIO pin" + self.sensor + " is " +new_state
            #     print s


    # write File
    # senserState : boolean: indicate whether isOccupied
    # sensorID : sensor's id
    def writeFile(self, sensorId, sensorState):
        self.fh = open("currentStateFinal.txt", "w")

        if sensorState:
            state = 1
        else:
            state = 0
        content = str(sensorId) + " " + str(state) + "\n"

        self.fh.write(str(content) + " ")
        # self.fh.flush()
        self.fh.close()



pir = PirTest()
pir.execute()
