# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.x0 = 10
    data.y0 = 10
    data.x1 = 200
    data.y1 = 200

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    drawLinePattern(canvas,data.x0,data.y0,data.x1,data.y1)


def drawLinePattern(canvas,x1,y1,x2,y2):
    drawV(canvas,x1,y1,x1,y2,(x1+x2)/2,y1,'blue')
    drawV(canvas,x1,y2,(x1+x2)/2,y1,x2,y2,'red')

def drawV(canvas,x1,y1,x2,y2,x3,y3,lineColor):
    canvas.create_line(x1,y1,x2,y2,width = 3,fill = lineColor)
    canvas.create_line(x2,y2,x3,y3,width = 3,fill = lineColor)
    drawGrid(canvas,x1,y1,x2,y2,x3,y3)

def drawGrid(canvas,x1,y1,x2,y2,x3,y3):
    dxStart = (x2 - x1)/20
    dyStart = (y2 - y1)/20
    dxEnd = (x3 - x2)/20
    dyEnd = (y3 - y2)/20
    for i in range (20):
        canvas.create_line(x1+i*dxStart,y1+i*dyStart,x2+i*dxEnd,y2+i*dyEnd,
            fill = "blue")
        # canvas.create_line(x1+1*dxStart,y1+1*dyStart,x2+1*dxEnd,y2-1*dyEnd)

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
