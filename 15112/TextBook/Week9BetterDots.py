######################################################
# Struct Example:  dotsDemo
######################################################

import random
# from structClass import Struct # defined above (saved in structClass.py)
from tkinter import *

class Dot(object): 
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.r = random.randint(20,50)
        self.color = random.choice(["pink","orange","yellow",
                                "green","cyan","purple"])
        self.clickCount = 0

    def containPoint(self,x,y):
        d = ((self.x - x)**2 + (self.y - y)**2)**0.5
        return (d <= self.r)
    def drawDot(self,canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r,
                           self.x+self.r, self.y+self.r,
                           fill = self.color)
        canvas.create_text(self.x, self.y, text=str(self.clickCount))

def init(data):
    data.dots = [ ]


def mousePressed(event, data):
    for dot in reversed(data.dots):
        if (dot.containPoint(event.x, event.y)):
            dot.clickCount += 1
            return
    data.dots.append(Dot(event.x, event.y))

def redrawAll(canvas, data):
    for dot in data.dots:
        dot.drawDot(canvas)

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

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

