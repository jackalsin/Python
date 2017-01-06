# events-example2.py
# Demos timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

def init(data): # initiate data
    data.squareLeft = 50
    data.squareFill = "yellow"
    data.circleCenters = [ ]
    data.timerDelay = 250

def mousePressed(event, data): 
    newCircleCenter = (event.x, event.y)
    data.circleCenters.append(newCircleCenter)

def keyPressed(event, data):
    if (event.char == "d"):
        if (len(data.circleCenters) > 0):
            data.circleCenters.pop(0)
        else:
            print("No more circles to delete!")
    if (event.keysym == "Left"):
        sqRight = data.squareLeft + 100
        if (sqRight > 20):
            data.squareLeft -= 20
        else:
            data.squareLeft = 200

def timerFired(data):
    data.squareFill = "green" if (data.squareFill == "yellow") else "yellow"

def redrawAll(canvas, data):
    # draw the square
    canvas.create_rectangle(data.squareLeft, 50,
                            data.squareLeft+100, 150,
                            fill=data.squareFill)
    # draw the circles
    for circleCenter in data.circleCenters:
        (cx, cy) = circleCenter
        r = 20
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="cyan")
    # draw the text
    canvas.create_text(150,20,text="events-example2.py")
    canvas.create_text(150,40,text="Mouse clicks create circles")
    canvas.create_text(150,60,text="Pressing 'd' deletes circles")
    canvas.create_text(150,80,text="Left arrow moves square left")
    canvas.create_text(150,100,text="Timer changes color of square")

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
