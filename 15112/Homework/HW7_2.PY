# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import math

####################################
# customize these functions
####################################

def init(data):
    data.mode = "mainScreen"
    data.buttonWidth = data.width/2
    data.buttonHeight = data.height/8
    data.circleCenters = []
    data.circleMatrixNum = 9
    data.circleRadius = 20
    data.margin = 50
    data.canvasLTx = data.margin
    data.canvasLTy = data.margin
    data.canvasRBx = data.width - data.margin
    data.canvasRBy = data.height - data.margin
    data.circlePatternColors = ["red","green","yellow","blue"]

    # for Spiral
    data.spiralCircleCenters = []
    data.spiralCircleRadius = 5
    data.armNumbers = 28
    data.armCircleNum = 32

    # Adapted Snake
    printInstructions()

def mousePressed(event, data):
    if (data.mode == "mainScreen"): mainScreenMousePressed(event,data)
    elif (data.mode == "drawCirclePattern"): drawCirclePatternMousePressed(event,data)
    elif(data.mode == "playTetris"): playTetrisMousePressed(event,data)
    elif(data.mode == "drawSpiral"): drawSpiralMousePressed(event,data)
    elif(data.mode == "adaptedSnake"): adaptedSnakeMousePressed(event,data)
    elif(data.mode == "betterSideScroller"): betterSideScrollerMousePressed(event,data)

def keyPressed(event, data):
    if (data.mode == "mainScreen"): mainScreenKeyPressed(event,data)
    elif (data.mode == "drawCirclePattern"): drawCirclePatternKeyPressed(event,data)
    elif(data.mode == "playTetris"): playTetrisKeyPressed(event,data)
    elif(data.mode == "drawSpiral"): drawSpiralKeyPressed(event,data)
    elif(data.mode == "adaptedSnake"): adaptedSnakeKeyPressed(event,data)
    elif(data.mode == "betterSideScroller"): betterSideScrollerKeyPressed(event,data)

def timerFired(data):
    if (data.mode == "mainScreen"): mainScreenTimerFired(data)
    elif (data.mode == "drawCirclePattern"): drawCirclePatternTimerFired(data)
    elif(data.mode == "playTetris"): playTetrisTimerFired(data)
    elif(data.mode == "drawSpiral"): drawSpiralTimerFired(data)
    elif(data.mode == "adaptedSnake"): adaptedSnakeTimerFired(data)
    elif(data.mode == "betterSideScroller"): betterSideScrollerTimerFired(data)

def mainScreenTimerFired(data):
    # if (data.mode == "mainScreen"): mainScreenTimerFired(data)
    if (data.mode == "drawCirclePattern"): drawCirclePatternTimerFired(data)
    elif(data.mode == "playTetris"): playTetrisTimerFired(data)
    elif(data.mode == "drawSpiral"): drawSpiralTimerFired(data)
    elif(data.mode == "adaptedSnake"): adaptedSnakeTimerFired(data)
    elif(data.mode == "betterSideScroller"): betterSideScrollerTimerFired(data)

def mainScreenKeyPressed(event,data):
    print(event.char)
    if event.char == 't':
        data.mode = "playTetris"
    elif event.char == 'c':
        data.mode = "drawCirclePattern"
    elif event.char == "s":
        data.mode = "drawSpiral"
    elif event.char == "a":
        data.mode = "adaptedSnake"
    elif event.char == "b":
        data.mode = "betterSideScroller"

def mainScreenMousePressed(event,data):
    # if (data.mode == "mainScreen"): mainScreenMousePressed(event,data)
    if (data.mode == "drawCirclePattern"): drawCirclePatternMousePressed(event,data)
    elif(data.mode == "playTetris"): playTetrisMousePressed(event,data)
    elif(data.mode == "drawSpiral"): drawSpiralMousePressed(event,data)
    elif(data.mode == "adaptedSnake"): adaptedSnakeMousePressed(event,data)
    elif(data.mode == "betterSideScroller"): betterSideScrollerMousePressed(event,data)

def mainScreenRedrawAll(canvas,data):
    canvas.create_text(data.width/2, data.height/12,
        text = "    Homework 7\n Name: Zhiwei Xin\n  Andrew ID: zxin", 
                    fill = "black",  font="Helvetica 26 bold")
    canvas.create_text(data.width/2, data.height/12*3,text = "playTetris (t)", 
                    fill = "black",  font="Helvetica 26 bold underline")
    canvas.create_text(data.width/2, data.height/12*5,text ="drawCirclePattern (c)", 
                    fill = "black",  font="Helvetica 26 bold underline")
    canvas.create_text(data.width/2, data.height/12*7,text = "drawSpiral (s)", 
                    fill = "black",  font="Helvetica 26 bold underline")
    canvas.create_text(data.width/2, data.height/12*9,text = "adaptedSnake (a)", 
                    fill = "black",  font="Helvetica 26 bold underline")    
    canvas.create_text(data.width/2, data.height/12*11,
                            text = "betterSideScroller (b)", fill = "black",
                            font="Helvetica 26 bold underline")
 
    createScreenButton(canvas,data,6)


def createScreenButton(canvas,data,buttonNumbers):
    for i in range(0,buttonNumbers):
        canvas.create_rectangle(data.width/2-data.buttonWidth/2, 
            data.height/12*(2*i+1)-data.buttonHeight/2, 
            data.width/2 +data.buttonWidth/2,
            data.height/12*(2*i+1)+data.buttonHeight/2)
    

def redrawAll(canvas, data):
    if (data.mode == "mainScreen"):
        mainScreenRedrawAll(canvas,data)
    elif (data.mode == "playTetris"):
        playTetrisRedrawAll(canvas,data) 
    elif (data.mode == "drawCirclePattern"):
        drawCirclePatternRedrawAll(canvas,data)     
    elif (data.mode == "drawSpiral"):
        drawSpiralRedrawAll(canvas,data) 
    elif (data.mode == "adaptedSnake"):
        adaptedSnakeRedrawAll(canvas,data)    
    elif (data.mode == "betterSideScroller"):
        betterSideScrollerRedrawAll(canvas,data) 





###### PlayTetris
def playTetrisKeyPressed(event,data):
    print("playTetrisKeyPressed(canvas,data)")
    if (event.keysym == "Escape"):
        data.mode = "mainScreen"



def playTetrisTimerFired(data):
    # print("playTetrisTimerFired(canvas,data)")
    pass


def playTetrisMousePressed(event,data):
    print( "playTetrisMousePressed(canvas,data)")


def playTetrisRedrawAll(canvas,data):
    canvas.create_text(data.width/2,data.height/2,text = "playTetrisRedrawAll(canvas,data)")
    




#### drawCirclePatternRedrawAll


def drawCirclePatternKeyPressed(event,data):
    if (event.keysym == "Escape"):
        data.mode = "mainScreen"
    elif event.keysym == "Down":
        data.circleMatrixNum = max(data.circleMatrixNum-1,1)
    elif event.keysym == "Up":
        data.circleMatrixNum = min(data.circleMatrixNum+1,
                    int((data.canvasRBx-data.canvasLTx)//data.circleRadius/2))


def drawCirclePatternTimerFired(data):
    # print("drawCirclePatternTimerFired(canvas,data)")
    pass


def drawCirclePatternMousePressed(event,data):
    print( "drawCirclePatternMousePressed(canvas,data)")


def drawCirclePatternRedrawAll(canvas,data):
    canvas.create_text(data.width/2,0,text = "Press ESC to exit", anchor = N,
                            font="Helvetica 26 bold underline")
    createCircleCenterList(data)
    drawOutLine(canvas,data)
    drawCircleMatrix(canvas,data)

def drawOutLine(canvas,data):
    xLT = data.circleCenters[0][0]-data.circleRadius
    yLT = data.circleCenters[0][1]-data.circleRadius
    xRB = data.circleCenters[-1][0]+data.circleRadius
    yRB = data.circleCenters[-1][1]+data.circleRadius
    canvas.create_rectangle(xLT,yLT,xRB,yRB,width = 3)

def createCircleCenterList(data):
    (cols,rows) = (data.circleMatrixNum,data.circleMatrixNum)
    data.circleCenters=[]    
    for row in range(rows):
        for col in range (cols):
            data.circleCenters.append(
                [data.canvasLTx+data.circleRadius*(col*2+1),
                data.canvasLTy+data.circleRadius*(row*2+1)])
    
def drawCircleMatrix(canvas, data):
    cols,rows = data.circleMatrixNum,data.circleMatrixNum
    r = data.circleRadius
    for row in range(rows):
        for col in range(cols):
            (cx,cy) = data.circleCenters[cols*row+col]
            if (col+row)%4 == 0:
                circleColor = data.circlePatternColors[0] # red
            elif row%3 == 0:
                circleColor = data.circlePatternColors[1] # green
            elif col % 2 ==1:
                circleColor = data.circlePatternColors[2] # yellow
            else:
                circleColor = data.circlePatternColors[3] # blue
            drawBullEye(canvas,cx,cy,r,circleColor)
           
def drawBullEye(canvas,cx,cy,r,circleColor):
    while(r>=1):
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r, fill = circleColor)
        r = r*2/3

# drawSpiralRedrawAll
def drawSpiralKeyPressed(event,data):
    print("drawSpiralKeyPressed(canvas,data)")
    if (event.keysym == "Escape"):
        data.mode = "mainScreen"
    elif(event.keysym == "Up"):
        data.spiralCircleRadius *= 1.1
    elif (event.keysym == "Down"):
        data.spiralCircleRadius = max(data.spiralCircleRadius*0.9, 1)


def drawSpiralTimerFired(data):
    timerDelay = 10*1000




def drawSpiralMousePressed(event,data):
    print( "drawSpiralMousePressed(canvas,data)")

def drawSpiralRedrawAll(canvas,data):
    canvas.create_text(data.width/2,100,text = "Press ESC to exit",
                            font="Helvetica 26 bold underline")
    data.spiralCircleCenters = []
    createSpiralsCircleCenters(canvas,data)
    drawSpiral(canvas,data)

def drawSpiral(canvas,data):
    arms = len(data.spiralCircleCenters)
    circles = len(data.spiralCircleCenters[0])
    r = data.spiralCircleRadius
    
    for arm in range(arms):
        for circle in range(circles):
            (cx,cy) = (data.spiralCircleCenters[arm][circle][0],
                        data.spiralCircleCenters[arm][circle][1])
            circleColor = rgbString((123+7*int(r)-(circle) * 3)%255,
                                    (123-3*int(r) +circle * 3)%255,
                                    (73*int(r) + circle * 3)%255)
            canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill = circleColor,width = 0)

def rgbString(red, green, blue): # cited from the course website
    return "#%02x%02x%02x" % (red, green, blue)

def createSpiralsCircleCenters(canvas, data):
    dTheta = math.pi * 2/data.armNumbers
    theta = 0
    for i in range (data.armNumbers):
        theta += dTheta
        data.spiralCircleCenters.append(spiralArmList(theta,data))

def spiralArmList(theta,data):
    startX = data.width/2 + data.spiralCircleRadius * math.cos(theta)
    startY = data.height/2 + data.spiralCircleRadius * math.sin(theta)
    dAlpha = math.pi/4/data.armCircleNum
    armList = []
    for i in range(data.armCircleNum):
        armList.append([startX,startY])
        startX += 2 * data.spiralCircleRadius * math.cos(theta+i * dAlpha)
        startY += 2 * data.spiralCircleRadius * math.sin(theta+i * dAlpha)

    return armList




# adaptedSnakeRedrawAll
def printInstructions():
    print("""Snake!\nUse the arrow keys to move the snake.
            Eat food to grow.
            Stay on the board!
            And don't crash into yourself!""")


def adaptedSnakeKeyPressed(event,data):
    print("adaptedSnakeKeyPressed(canvas,data)")
    if (event.keysym == "Escape"):
        data.mode = "mainScreen"



def adaptedSnakeTimerFired(data):
    # print("drawCirclePatternTimerFired(canvas,data)")
    pass


def adaptedSnakeMousePressed(event,data):
    print( "adaptedSnakeMousePressed(canvas,data)")

def adaptedSnakeRedrawAll(canvas,data):

    canvas.create_text(data.width/2,data.height/2,text = "adaptedSnakeRedrawAll(canvas,data)")



# betterSideScrollerRedrawAll
def betterSideScrollerKeyPressed(event,data):
    print("betterSideScrollerKeyPressed(canvas,data)")
    if (event.keysym == "Escape"):
        data.mode = "mainScreen"



def betterSideScrollerTimerFired(data):
    # print("drawCirclePatternTimerFired(canvas,data)")
    pass


def betterSideScrollerMousePressed(event,data):
    print( "betterSideScrollerMousePressed(canvas,data)")


def betterSideScrollerRedrawAll(canvas,data):
    canvas.create_text(data.width/2,data.height/2,text = "betterSideScrollerRedrawAll(canvas,data)")



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

run(900, 900)
