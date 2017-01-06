# events-example1.py
# Demos timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.mouseText = "No mousePresses yet"
    data.keyText = "No keyPresses yet"
    data.timerText = "No timerFired calls yet"
    data.timerCounter = 0
    data.timerDelay = 250 # milliseconds

def mousePressed(event, data):
    data.mouseText = "last mousePressed: " + str((event.x, event.y))

def keyPressed(event, data):
    data.keyText = ("last keyPressed: char=" + event.char + 
                    ", keysym=" + event.keysym)

def timerFired(data):
    data.timerCounter += 1
    data.timerText = "timerCounter = " + str(data.timerCounter)

def redrawAll(canvas, data):
    canvas.create_text(data.width/2, 20, text="events-example1.py")
    canvas.create_text(data.width/2, 40, text=data.mouseText)
    canvas.create_text(data.width/2, 60, text=data.keyText)
    canvas.create_text(data.width/2, 80, text=data.timerText)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 200)
