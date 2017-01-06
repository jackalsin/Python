# Name: Zhiwei Xin
# Andrew ID: zxin


from tkinter import *
import math
import random

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
    if data.mode =='adaptedSnake':
        printInstructions()
    data.snakeBoard = []
    data.snakeBoardRows = 10
    data.snakeBoardCols = 10
    data.snakeBoardMargin = 5
    data.snakeCellSize = 30
    data.headRow = 0
    data.headCol = 0
    data.inDebugMode = False
    data.isGameOver = False
    loadSnakeBoard(data)
    data.snakeDrow = 1
    data.snakeDcol = 0
    data.timerDelay = 250*4
    data.ignoreNextTimerEvent = False
    data.paused = False
    
    # scroller // cited from the course website
    data.scrollX = 0  # amount view is scrolled to the right
    data.scrollMargin = 50 # closest player may come to either canvas edge
    data.playerX = data.scrollMargin # player's left edge
    data.playerY = 0  # player's bottom edge (distance above the base line)
    data.playerWidth = 10
    data.playerHeight = 20
    data.playerHorizonSpeed = 0
    data.playerVerticalSpeed = 0
    data.jumpFlag = False
    data.jumpTime0 = 10
    data.jumpTime = data.jumpTime0
    data.bounceSpeed = 40
    data.walls = 16
    data.wallPoints = [0]*data.walls
    data.wallAlreadyHits = [False] * data.walls
    data.wallWidth = 20
    data.wallHeight = 40
    data.wallSpacing = 90 # wall left edges are at 90, 180, 270,...
    data.currentWallHit = -1 # start out not hitting a wall
    data.jumpPosition = 0
    data.landPosition = 0
    data.waterBalloons = []
    data.waterBalloonSpeed = 10
    data.waterBalloonInitialPosition = 0
    data.waterBalloonY = -2/3*data.playerHeight+data.height/2
    data.waterBalloonRadius = 5
    data.destroyedWallNumList = []


def mousePressed(event, data):
    if (data.mode == "mainScreen"): mainScreenMousePressed(event,data)
    elif (data.mode == "drawCirclePattern"): 
        drawCirclePatternMousePressed(event,data)
    elif(data.mode == "playTetris"): playTetrisMousePressed(event,data)
    elif(data.mode == "drawSpiral"): drawSpiralMousePressed(event,data)
    elif(data.mode == "adaptedSnake"): adaptedSnakeMousePressed(event,data)
    elif(data.mode == "betterSideScroller"): 
        betterSideScrollerMousePressed(event,data)

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
        text = "Homework 7", 
                    fill = "black",  font="Helvetica 26 bold")
    canvas.create_text(data.width/2, data.height/12*3,text = 
                                    "Name: Zhiwei Xin\n Andrew ID: zxin ", 
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






#### drawCirclePatternRedrawAll


def drawCirclePatternKeyPressed(event,data):
    if (event.keysym == "Escape"):
        data.mode = "mainScreen"
        init(data)
    elif event.keysym == "Down":
        data.circleMatrixNum = max(data.circleMatrixNum-1,1)
    elif event.keysym == "Up":
        data.circleMatrixNum = min(data.circleMatrixNum+1,
                    int((data.canvasRBx-data.canvasLTx)//data.circleRadius/2))


def drawCirclePatternTimerFired(data):
    pass


def drawCirclePatternMousePressed(event,data):
    pass

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
    if (event.keysym == "Escape"):
        data.mode = "mainScreen"
        init(data)

    elif(event.keysym == "Up"):
        data.spiralCircleRadius *= 1.1
    elif (event.keysym == "Down"):
        data.spiralCircleRadius = max(data.spiralCircleRadius*0.9, 1)


def drawSpiralTimerFired(data):
    data.timerDelay = 10*1000





def drawSpiralMousePressed(event,data):
    pass

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
    xMax = data.width/2
    yMax = data.height/2
    xMin = data.width/2
    yMin = data.height/2

    for arm in range(arms):
        for circle in range(circles):
            (cx,cy) = (data.spiralCircleCenters[arm][circle][0],
                        data.spiralCircleCenters[arm][circle][1])
            xMax = max(xMax,cx+r); xMin = min(xMin,cx-r)
            yMax = max(yMax,cy+r); yMin = min(yMin, cy-r)
            circleColor = rgbString((123+7*int(r)-(circle) * 3)%255,
                                    (123-3*int(r) +circle * 3)%255,
                                    (73*int(r) + circle * 3)%255)
            canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill = circleColor,width = 0)

    drawSpiralOutline(canvas,data,xMax,xMin,yMax,yMin)
    

def drawSpiralOutline(canvas,data,xMax,xMin,yMax,yMin):
    margin = 10
    canvas.create_rectangle(xMin-margin,yMin-margin,xMax+margin,yMax+margin,
        width = 5)




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
# cited from http://www.kosbie.net/cmu/fall-11/15-112/handouts/snake/snake.html

def printInstructions():
    print("""Snake!\nUse the arrow keys to move the snake.
Eat food to grow.
Stay on the board!
And don't crash into yourself!""")


def adaptedSnakeKeyPressed(event,data):
    data.ignoreNextTimerEvent = True
    if (event.keysym == "Escape"):
        data.mode = "mainScreen"
        init(data)
    elif (event.keysym == "p"): data.paused = True; return
    if (event.char == "q"):
        gameOver(data)
    elif (event.char == "r"):
        init(data)
        data.mode == "adaptedSnake"

    elif (event.char == "d"):
        data.inDebugMode = not data.inDebugMode
    # now process keys that only work if the game is not over
    if (data.isGameOver == False):
        if (event.keysym == "Up"):
            moveSnake(-1, 0,data)
        elif (event.keysym == "Down"):
            moveSnake(+1, 0,data)
        elif (event.keysym == "Left"):
            moveSnake(0,-1,data)
        elif (event.keysym == "Right"):
            moveSnake(0,+1,data)

def gameOver(data):
    data.isGameOver = True

def adaptedSnakeTimerFired(data):
    ignoreThisTimerEvent = data.ignoreNextTimerEvent
    data.ignoreNextTimerEvent = False
    if (data.paused == True): return
    if ((data.isGameOver == False) and (ignoreThisTimerEvent == False)):
        # only process timerFired if game is not over
        drow = data.snakeDrow
        dcol = data.snakeDcol
        moveSnake(drow, dcol,data)


def adaptedSnakeMousePressed(event,data):
    pass

def adaptedSnakeRedrawAll(canvas,data):
    canvas.create_text(data.width-data.margin,data.height-data.margin,
        text = """Press ESC to exit\nPress Arrow to play\nPress P to pause\nPress q to quit
Press r to restart\nPress D to Debug""",anchor = SE, font="Helvetica 17 bold ")

    drawSnakeBoard(canvas,data)



def drawSnakeBoard(canvas,data):
    rows = len(data.snakeBoard)
    cols = len(data.snakeBoard[0])
    for row in range (rows):
        for col in range (cols):
            drawSnakeCell(canvas,data,row,col)

def drawSnakeCell(canvas,data,row,col):
    margin = data.snakeBoardMargin
    cellSize = data.snakeCellSize
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left,top,right,bottom,fill = "white")
    if (data.snakeBoard[row][col] > 0):
        canvas.create_oval(left,top,right,bottom,fill = "blue")
    elif (data.snakeBoard[row][col] < 0):
        # draw food
        canvas.create_oval(left, top, right, bottom, fill="green")

    if (data.inDebugMode == True):
        canvas.create_text(left+cellSize/2,top+cellSize/2,
                            text=str(data.snakeBoard[row][col]))


def loadSnakeBoard(data):
    rows = data.snakeBoardRows
    cols = data.snakeBoardCols
    data.snakeBoard = [ [0] * cols for row in range(rows) ]
    data.snakeBoard[rows//2][cols//2] = 1

    findSnakeHead(data)
    placeFood(data)

def placeFood(data):
    # place food (-1) in a random location on the snakeBoard, but
    # keep picking random locations until we find one that is not
    # part of the snake!
    snakeBoard = data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    while True:
        row = random.randint(0,rows-1)
        col = random.randint(0,cols-1)
        if (snakeBoard[row][col] == 0):
            break
    snakeBoard[row][col] = -1

def moveSnake(drow, dcol,data):
    # move the snake one step forward in the given directio.
    data.snakeDrow = drow # store direction for next timer event
    data.snakeDcol = dcol
    snakeBoard = data.snakeBoard
    headRow = data.headRow
    headCol = data.headCol
    newHeadRow = headRow + drow
    newHeadCol = headCol + dcol
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])

    if ((newHeadRow < 0) or (newHeadRow >= rows) or
        (newHeadCol < 0) or (newHeadCol >= cols)):
        # snake ran off the board
        gameOver(data)
    elif (snakeBoard[newHeadRow][newHeadCol] > 0):
        # snake ran into itself!
        gameOver(data)
    elif (snakeBoard[newHeadRow][newHeadCol] < 0):
        # eating food!  Yum!
        snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol];
        data.headRow = newHeadRow
        data.headCol = newHeadCol
        placeFood(data)
    else:
        snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol];
        data.headRow = newHeadRow
        data.headCol = newHeadCol
        removeTail(data)

def removeTail(data):
    # find every snake cell and subtract 1 from it.  When we're done,
    # the old tail (which was 1) will become 0, so will not be part of the snake.
    # So the snake shrinks by 1 value, the tail.
    snakeBoard = data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > 0):
                snakeBoard[row][col] -= 1

def findSnakeHead(data):
    # find where snakeBoard[row][col] is largest, and
    # store this location in headRow, headCol
    snakeBoard = data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    headRow = 0
    headCol = 0
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > snakeBoard[headRow][headCol]):
                headRow = row
                headCol = col
    data.headRow = headRow
    data.headCol = headCol





# betterSideScrollerRedrawAll


def betterSideScrollerKeyPressed(event,data):
    if (event.keysym == "Escape"):
        data.mode = "mainScreen"
        init(data)
    elif event.keysym == 'Right':
        data.playerHorizonSpeed+=1
    elif event.keysym == "Left":
        data.playerHorizonSpeed-=1   
    elif (event.keysym == "Up"):    
        if data.jumpFlag == False:
            data.jumpFlag = True
            data.jumpPosition = data.playerX # landPosition un written
    elif (event.keysym == "Down"):
        data.playerVerticalSpeed-=1
    elif (event.keysym == "t"):
        waterFire(data)

def waterFire(data):
    if data.playerHorizonSpeed >= 0:
        waterBalloonSpeed = 1.1*data.playerHorizonSpeed + 10
    else:
        waterBalloonSpeed = 1.1 * data.playerHorizonSpeed - 10
    waterBalloonInitialPosition = data.playerX + data.playerWidth
    data.waterBalloons.append([waterBalloonInitialPosition,waterBalloonSpeed])

def jumpSpeed(data):
    data.playerVerticalSpeed = (data.bounceSpeed - 
        2*data.bounceSpeed/data.jumpTime0 * (data.jumpTime0 - data.jumpTime))

def betterSideScrollerTimerFired(data):
    data.timerDelay = 100
    if data.jumpFlag == True:
        jumpSpeed(data)
        data.jumpTime -= 1

    movePlayer(data.playerHorizonSpeed,data.playerVerticalSpeed,data)  

    if data.jumpTime == -1: # reset 
        data.jumpTime = 10
        data.jumpFlag = False
        data.playerVerticalSpeed = 0
        data.playerY = 0
        data.landPosition = data.playerX
        checkScoreWall(data)

    moveWaterBalloon(data)
    makeSureWaterInScroll(data)
    waterDestroy(data)

def makeSureWaterInScroll(data):
    water = 0
    while(water < len(data.waterBalloons)):
        # print("debug",water,len(data.waterBalloons))
        r = data.waterBalloonRadius
        position = data.waterBalloons[water][0]
        scrollLeft = data.scrollX
        scrollRight = scrollLeft + data.width

        if(((position + r) <= scrollLeft) or ((position - r) <= scrollLeft)
            or ((position + r) >= scrollRight) or
             ((position - r) >= scrollRight)):
            data.waterBalloons.pop(water)
        water+=1


def waterDestroy(data):
    # check water hits wall and wall in the scroll 
    # check water hits scroll right
    for water in range(len(data.waterBalloons)):
        (waterX1,waterX2) = getWaterBoundary(data,water)
        for wall in range(data.walls):
            (wallLeft,y0,wallRight,y1) = getWallBounds(wall,data)
            if ((wallLeft <= waterX1 <= wallRight) or
                 (wallLeft <= waterX2 <= wallRight)):
                data.destroyedWallNumList.append(wall)


def getWaterBoundary(data,waterNum):
    (positionX, waterSpeed) = data.waterBalloons[waterNum]
    r = data.waterBalloonRadius
    positionY = data.waterBalloonY
    (xLT,xRT) = (positionX-r,positionY+r)
    return (xLT,xRT)


def moveWaterBalloon(data):
    if (len(data.waterBalloons) == 0):
        return
    else:
        for waterBalloonNum in range(len(data.waterBalloons)):
            (waterBalloonPosition, 
                waterBalloonSpeed) = data.waterBalloons[waterBalloonNum]
            waterBalloonPosition += waterBalloonSpeed
            data.waterBalloons[waterBalloonNum] = (waterBalloonPosition,
                                                        waterBalloonSpeed)
def checkScoreWall(data):
    for wallNum in range (data.walls):
        (x0,y0,x1,y1) = getWallBounds(wallNum,data)
        if (((data.jumpPosition - x0) * (data.landPosition - x0) < 0)
            and ((data.jumpPosition - x1) * (data.landPosition - x1) < 0)):
            data.wallPoints[wallNum]+=1

    # reset land and jump position
    data.landPosition = 0
    data.jumpPosition = 0

def betterSideScrollerMousePressed(event,data):
    pass

def betterSideScrollerRedrawAll(canvas,data): # cited from the course website
    # draw the base line
    lineY = data.height/2
    lineHeight = 5
    canvas.create_rectangle(0, lineY, data.width, lineY+lineHeight,fill="black")

    # draw the walls
    # (Note: should optimize to only consider walls that can be visible now!)
    sx = data.scrollX
    for wall in range(data.walls):
        if wall in data.destroyedWallNumList:
            continue
        (x0, y0, x1, y1) = getWallBounds(wall, data)
        fill = "orange" if (wall == data.currentWallHit) else "pink"
        canvas.create_rectangle(x0-sx, y0, x1-sx, y1, fill=fill)
        (cx, cy) = ((x0+x1)/2 - sx, (y0 + y1)/2)
        canvas.create_text(cx, cy, text=str(data.wallPoints[wall]))
        cy = lineY + 5
        canvas.create_text(cx, cy, text=str(wall), anchor=N)

    # draw the player
    (x0, y0, x1, y1) = getPlayerBounds(data)
    canvas.create_oval(x0 - sx, y0, x1 - sx, y1, fill="cyan")

    # draw the instructions
    msg = "Use arrows to move, hit walls to score"
    canvas.create_text(data.width/2, 20, text=msg)
    drawWaterBalloons(canvas,data)

def drawWaterBalloons(canvas,data):
    r = data.waterBalloonRadius
    for balloon in range(len(data.waterBalloons)):
        (positionX, waterSpeed) = data.waterBalloons[balloon]
        canvas.create_oval(positionX-r,data.waterBalloonY-r,
                    positionX+r,data.waterBalloonY+r,fill = "blue",width = 0)

def getPlayerBounds(data): # cited from the course website
    # returns absolute bounds, not taking scrollX into account
    (x0, y1) = (data.playerX, data.height/2 - data.playerY)
    (x1, y0) = (x0 + data.playerWidth, y1 - data.playerHeight)
    return (x0, y0, x1, y1)

def getWallBounds(wall, data):# cited from the course website
    # returns absolute bounds, not taking scrollX into account
    (x0, y1) = ((1+wall) * data.wallSpacing, data.height/2)
    (x1, y0) = (x0 + data.wallWidth, y1 - data.wallHeight)
    return (x0, y0, x1, y1)

def getWallHit(data):# cited from the course website
    # return wall that player is currently hitting
    # note: this should be optimized to only check the walls that are visible
    # or even just directly compute the wall without a loop
    playerBounds = getPlayerBounds(data)
    for wall in range(data.walls):
        wallBounds = getWallBounds(wall, data)
        if (boundsIntersect(playerBounds, wallBounds) == True):
            return wall
    return -1

def boundsIntersect(boundsA, boundsB):# cited from the course website
    # return l2<=r1 and t2<=b1 and l1<=r2 and t1<=b2
    (ax0, ay0, ax1, ay1) = boundsA
    (bx0, by0, bx1, by1) = boundsB
    return ((ax1 > bx0) and (bx1 > ax0) and
            (ay1 > by0) and (by1 > ay0))


def movePlayer(dx, dy, data):# cited from the course website
    data.playerX += dx
    data.playerY += dy
    # scroll to make player visible as needed
    if (data.playerX < data.scrollX + data.scrollMargin):
        data.scrollX = data.playerX - data.scrollMargin
    if (data.playerX > data.scrollX + data.width - data.scrollMargin):
        data.scrollX = data.playerX - data.width + data.scrollMargin
    # and check for a new wall hit
    wall = getWallHit(data)
    if (wall != data.currentWallHit):
        data.currentWallHit = wall
        if ((wall >= 0) and (wall not in data.destroyedWallNumList)):
            data.playerHorizonSpeed = 0 # stop when the player hits
            # position the player in the left
            wallLeft = getWallBounds(wall,data)[0]
            data.playerX = wallLeft - data.playerWidth - 1 
            # -1 in order not to overlap
            data.playerY = 0
            if (data.wallAlreadyHits[wall] == False) :
                data.wallPoints[wall] = max(0,data.wallPoints[wall] - 1)
                data.wallAlreadyHits[wall] = True




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





####################################
# testFunction 
####################################

class StructTest(object): pass
data2 = StructTest()
def init(data2):
    data2.isGameOver = False

def gameOver(data):
    data.isGameOver = True


def testGameOver(data2):
    print("Testing gameOver()...", end = '')
    gameOver(data2)
    assert(data2.isGameOver == True)
    print("passed")


def testAll():
    init(data2)
    testGameOver(data2)

testAll()