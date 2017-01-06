# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import random

class Square(object):
    """docstring for Square"""
    def __init__(self, direction, data):
        self.direction = direction
        self.x = data.width/2
        self.y = data.height/2
        self.size = random.randint(10,50)
        self.color = "yellow"
        self.color1 = "yellow"
        self.color2 = "black"
        self.canMove = True


    def drawSelf(self, canvas, data):
        canvas.create_rectangle(self.x - self.size/2, self.y - self.size/2, 
                                self.x + self.size/2, self.y + self.size/2 
                                ,fill = self.color)
    def move(self):
        if self.canMove:
            dx = self.direction[0]
            dy = self.direction[1]
            self.x += dx
            self.y += dy

    def getCorList(self):
        return [(self.x - self.size/2, self.y - self.size/2), 
                                (self.x + self.size/2, self.y + self.size/2)]
####################################
# customize these functions
####################################

def init(data):
    dirs = [(1,1),(-1,-1),(-1,1),(1,-1)]
        # NE, SW, SE, NW
    data.squareList = []
    for i in range(len(dirs)):
        data.squareList.append(Square(dirs[i],data))

    data.count = 10
    data.gameOver = False
    data.time = 0

def mousePressed(event, data):
    # use event.x and event.y
    for sq in data.squareList:
        corList = sq.getCorList()
        LTX = corList[0][0]
        LTY = corList[0][1]
        RBX = corList[1][0]
        RBY = corList[1][1]
        if LTX <= event.x <= RBX and LTY <= event.y <= RBY:
            sq.canMove = not sq.canMove
    

def keyPressed(event, data):
    init(data)

def timerFired(data):
    data.timerDelay = 100
    if data.gameOver == False:
        data.count += 1
        move(data)
        checkBounce(data)

        for sq in data.squareList:
            if sq.direction == (1,-1) or sq.direction == (1,1):
                if data.count % 5 == 0:
                    if sq.color == sq.color1:
                        sq.color = sq.color2
                    else:
                        sq.color = sq.color1
            else:
                if data.count % 5 == 0:
                    sq.size += 1

        
        if data.count == 100:
            data.gameOver = True

def redrawAll(canvas, data):
    for i in data.squareList:
        i.drawSelf(canvas,data)
    drawTimer(canvas, data)
    if data.gameOver == True:
        canvas.create_text(data.width/2, data.height/2, text = "Game Over")

def drawTimer(canvas,data):
    time = data.count/1000
    canvas.create_text(data.width/2, 20,text = str(time))
def move(data):
    for sq in data.squareList:
        sq.move()

def checkBounce(data):
    for sq in data.squareList:
        corList = sq.getCorList()
        if (corList[0][0]<= 0 or corList[0][0]>= data.width 
            or corList[0][1] <= 0 or corList[0][1] >= data.height
            or corList[1][0] <= 0 or corList[1][0] >= data.width
            or corList[1][0] <=0 or corList[1][1] >= data.height):
            sq.direction = (-sq.direction[0], -sq.direction[1])

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
    data.timerDelay = 10 # milliseconds
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

run(400, 400)
