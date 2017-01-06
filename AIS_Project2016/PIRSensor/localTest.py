import RPi.GPIO as GPIO
import time

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False


def writeFile( sensorId, sensorState):
    fh = open("currentStateFinal.txt", "w")

    if sensorState:
        state = 1
    else:
        state = 0
    content = str(sensorId) + " " + str(state) + "\n"

    fh.write(str(content) + " ")
    # self.fh.flush()
    fh.close()


while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    print current_state
    writeFile(sensor, current_state)

