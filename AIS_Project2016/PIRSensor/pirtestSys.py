import time
import os, sys

from client import Client

TRIGGER_TIME = 5
JUDGE_TIME = 15

class PirTest(object):

    def __init__(self):
        self.sensor = 4

        self.zeroCount = 0
        self.hasSomeone = False
        self.client = Client()

        # self.fh = open("currentStateFinal.txt", "a")
        self.finalOuput = 0 # no one is zero, 1 is occupied.

    def execute(self):
        previous_state = False
        current_state = False
        self.zeroCount = 0
        while True:
            time.sleep(0.1)
            previous_state = current_state

            intput = raw_input("input a state\n")
            current_state = int (intput)
            # self.fh.write(str(current_state) + " ")
            if current_state == 1:
                self.zeroCount = 0
            else:
                self.zeroCount += 1
                self.zeroCount = min(self.zeroCount, 200)
            # self.count
            if (self.hasSomeone and self.zeroCount > JUDGE_TIME):
                # someone was there but left
                self.writerFile(self.sensor, self.hasSomeone)
                self.hasSomeone = False
                self.client.msg_send_to_sever("Sending from Pir:someone left")
                print "someone left"

            elif (not (self.hasSomeone) and self.zeroCount == 0):
                # no one there someone comes
                self.writerFile(self.sensor, self.hasSomeone)
                self.hasSomeone = True
                self.client.msg_send_to_sever("Sending from Pir:someone occupied")
                print "someone occupied"

            print "the self.count = " + str(self.zeroCount)




    # write File
    # senserState : boolean: indicate whether isOccupied
    # sensorID : sensor's id
    def writerFile(self, sensorId, sensorState):
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
