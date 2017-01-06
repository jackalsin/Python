
import turtle

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.n = 0


def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    print(event.keysym)
    if (event.keysym == "Up"):
        data.n+=1
    elif (event.keysym == "Down"):
        data.n = max(0,data.n - 1)
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    turtle.delay(0)
    turtle.speed(0)
    drawHFractal(data.width/2,data.n)
    turtle.done() 
    pass

def drawHFractal(length,n):
    if (n == 0):
        turtle.forward(length/2) # step 1
        turtle.left(90)
        turtle.forward(length/2) # step 2
        turtle.right(90)
        turtle.right(90)

        turtle.forward(length) # step 3 
        turtle.right(90)
        turtle.right(90)

        turtle.forward(length/2) # step 4
        turtle.left(90)
        turtle.forward(length) # step 5
        turtle.left(90)
        turtle.forward(length/2) # s6
        turtle.right(90)
        turtle.right(90)

        turtle.forward(length) # step 7
        turtle.right(90)
        turtle.right(90)

        turtle.forward(length/2)
        turtle.left(90)
        turtle.forward(length/2)

    else:
        turtle.forward(length/2) # step 1 go right !
        turtle.left(90)
        turtle.forward(length/2) # step 2
        turtle.right(90)

        drawHFractal(length/2,n-1)
        turtle.right(90)

        turtle.forward(length) # step 3 
        turtle.right(90)
        drawHFractal(length/2,n-1)
        turtle.right(90)

        turtle.forward(length/2) # step 4
        turtle.left(90)
        turtle.forward(length) # step 5
        turtle.left(90)
        turtle.forward(length/2) # step 6
        turtle.right(90)

        drawHFractal(length/2,n-1)
        turtle.right(90)

        turtle.forward(length) # step 7
        turtle.right(90)
        drawHFractal(length/2,n-1)
        turtle.right(90)

        turtle.forward(length/2) #step 8 
        turtle.left(90)
        turtle.forward(length/2) # step 9




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

run(800, 800)
