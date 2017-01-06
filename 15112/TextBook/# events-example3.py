# events-example3.py
# Demos timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.squareLeft = 50
    data.squareTop = 50
    data.squareFill = "yellow"
    data.squareSize = 25
    data.circleCenters = [ ]
    data.counter = 0
    data.headingRight = True
    data.headingDown = True
    data.isPaused = False
    data.timerDelay = 50

def mousePressed(event, data):
    newCircleCenter = (event.x, event.y)
    data.circleCenters.append(newCircleCenter)

def keyPressed(event, data):
    if (event.char == "d"):
        if (len(data.circleCenters) > 0):
            data.circleCenters.pop(0)
        else:
            print("No more circles to delete!")
    elif (event.char == "p"):
        data.isPaused = not data.isPaused
    elif (event.char == "s"):
        doStep(data)
    if (event.keysym == "Left"):
        moveLeft(data)
    elif (event.keysym == "Right"):
        moveRight(data)

def moveLeft(data):
    data.squareLeft -= 20

def moveRight(data):
    data.squareLeft += 20

def moveUp(data):
    data.squareTop -= 20

def moveDown(data):
    data.squareTop += 20

def timerFired(data):
    if (not data.isPaused): doStep(data)

def doStep(data):
    data.counter += 1
    if (data.counter % 5 == 0):
        data.squareFill = "green" if (data.squareFill == "yellow") else "yellow"
    if (data.headingRight == True):
        if (data.squareLeft + data.squareSize > data.width):
            data.headingRight = False
        else:
            moveRight(data)
    else:
        if (data.squareLeft < 0):
            data.headingRight = True
        else:
            moveLeft(data)
    if (data.headingDown == True):
        if (data.squareTop + data.squareSize > data.height):
            data.headingDown = False
        else:
            moveDown(data)
    else:
        if (data.squareTop < 0):
            data.headingDown = True
        else:
            moveUp(data)

def redrawAll(canvas, data):
    # draw the square
    canvas.create_rectangle(data.squareLeft,
                            data.squareTop,
                            data.squareLeft + data.squareSize,
                            data.squareTop + data.squareSize,
                            fill=data.squareFill)
    # draw the circles
    for circleCenter in data.circleCenters:
        (cx, cy) = circleCenter
        r = 20
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="cyan")
    # draw the text
    canvas.create_text(150,20,text="events-example3.py")
    canvas.create_text(150,40,text="Mouse clicks create circles")
    canvas.create_text(150,60,text="Pressing 'd' deletes circles")
    canvas.create_text(150,80,text="Pressing 'p' pauses/unpauses timer")
    canvas.create_text(150,100,text="Pressing 's' steps the timer once")
    canvas.create_text(150,120,text="Left arrow moves square left")
    canvas.create_text(150,140,text="Right arrow moves square right")
    canvas.create_text(150,160,text="Timer changes color of square")

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

run(300, 200)
