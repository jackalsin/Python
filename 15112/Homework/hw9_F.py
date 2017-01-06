from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.n = 0
    print(data.width,data.height)

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
    canvas.create_rectangle(0,0,data.width,data.height)
    drawHFractal(canvas,data.width/2,data.height/2,data.width/2,data.height/2,data.n)
    pass

def drawHFractal(canvas,cx ,cy ,width ,height,n):
    if (n == 0):
        xL, yL = cx - 0.5*width, cy
        xR, yR = cx + 0.5*width, cy
        x1, y1 = xL, yL - 0.5*height
        x2, y2 = xL, yL + 0.5*height
        x3, y3 = xR, yR - 0.5*height
        x4, y4 = xR, yR + 0.5*height
        canvas.create_line(x1,y1,x2,y2)
        canvas.create_line(x3,y3,x4,y4)
        canvas.create_line(xL,yL,xR,yR)
        return
    else:
        # draw hon
        xL, yL = cx - 0.5*width, cy
        xR, yR = cx + 0.5*width, cy
        x1, y1 = xL, yL - 0.5*height
        x2, y2 = xL, yL + 0.5*height
        x3, y3 = xR, yR - 0.5*height
        x4, y4 = xR, yR + 0.5*height

        canvas.create_line(x1,y1,x2,y2)
        canvas.create_line(x3,y3,x4,y4)
        canvas.create_line(xL,yL,xR,yR)

        drawHFractal(canvas,x1 ,y1 ,width/2 ,height/2,n-1)
        drawHFractal(canvas,x2 ,y2 ,width/2 ,height/2,n-1)
        drawHFractal(canvas,x3 ,y3 ,width/2 ,height/2,n-1)
        drawHFractal(canvas,x4 ,y4 ,width/2 ,height/2,n-1)
        return


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
