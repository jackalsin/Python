# Name: Zhiwei Xin
# Andrew ID: zxin

from tkinter import *
import math
import random 
import copy

def init(data):
    # set board dimensions and margin
    data.rows = 15
    data.cols = 10
    data.margin = 20
    # make board
    data.emptyColor = "blue"
    data.board = [([data.emptyColor] * data.cols) for row in range(data.rows)]
    data.paused = False
    data.scores = 0 
    ########### following are the Pieces we need ######
    #Seven "standard" pieces (tetrominoes)
    iPiece = [
                [ True,  True,  True,  True]
            ]
  
    jPiece = [
            [ True, False, False ],
            [ True, True,  True]
            ]
  
    lPiece = [
            [ False, False, True],
            [ True,  True,  True]
            ]
  
    oPiece =  [
            [ True, True],
            [ True, True]
            ]
  
    sPiece = [
                [ False, True, True],
                [ True,  True, False ]
            ]
  
    tPiece = [
                [ False, True, False ],
                [ True,  True, True]
            ]   

    zPiece = [
                [ True,  True, False ],
                [ False, True, True]
            ]
    tetrisPieces = [iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece]
    tetrisPieceColors = ["red", "yellow", "magenta", "pink", 
                                "cyan", "green", "orange" ]
    data.tetrisPieces = tetrisPieces
    data.tetrisPieceColors = tetrisPieceColors
   
    ############### above initial Pieces Attributes #############################
    
    ############## following are for fallingPiece
    data.fallingPieceShape = None 
    # [[False, True, False], [True, True, True]]
    data.fallingPieceColor = None
    data.fallingPieceRow = 0 # the top row
    data.fallingPieceCol = data.cols//2 # the left col 
    newFallingPiece(data)

    rowList = []
    colList = []
    data.fallenPiece = []
    for row in range(data.rows):
        colList = []
        for col in range(data.cols):
            colList.append([False,None])
        rowList.append(colList)
    data.fallenPiece = copy.deepcopy(rowList)

    data.isGameOver = False

def printList(data):
    rows = len(data.fallenPiece)
    cols = len(data.fallenPiece[0])
    for row in range(rows):
        for col in range(cols):
            print(data.fallenPiece[row][col], end = ",")
        print()


def newFallingPiece(data):
    pieceShapeIndex = random.randint(0,6)
    pieceColorIndex = random.randint(0,6)
    data.fallingPieceShape = data.tetrisPieces[pieceShapeIndex]
    data.fallingPieceColor = data.tetrisPieceColors[pieceColorIndex]
    pieceLength = len(data.fallingPieceShape[0])
    data.fallingPieceCol = data.cols//2 - pieceLength//2
    data.fallingPieceRow = 0




# getCellBounds from grid-demo.py
def getCellBounds(row, col, data):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = data.width - 2*data.margin
    gridHeight = data.height - 2*data.margin
    x0 = data.margin + gridWidth * col / data.cols
    x1 = data.margin + gridWidth * (col+1) / data.cols
    y0 = data.margin + gridHeight * row / data.rows
    y1 = data.margin + gridHeight * (row+1) / data.rows
    return (x0, y0, x1, y1)

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if (event.keysym == "r"):
        init(data)
    elif data.isGameOver == True:
        return
    elif (event.keysym == "p"):
        data.paused = not data.paused
    if data.paused == False:
        if (event.keysym == "Left"):
            moveFallingPiece(data,0,-1)
        elif (event.keysym == "Right"):
            moveFallingPiece(data,0,1)
        elif (event.keysym == "Down"):
            moveFallingPiece(data,1,0)
        elif (event.keysym == "Up"):
            rotateFallingPiece(data)


def timerFired(data):
    data.timerDelay = 500
    if ((data.isGameOver == True) or (data.paused == True)): # Game over
        return 
    if (moveFallingPiece(data, 1, 0) == False):
        placeFallingPiece(data)
        newFallingPiece(data)
        if isLegalMove(data) == False:
            data.isGameOver = True

def placeFallingPiece(data):
    startRow = data.fallingPieceRow
    startCol = data.fallingPieceCol
    pieceRows = len(data.fallingPieceShape)
    pieceCols = len(data.fallingPieceShape[0])
    color = data.fallingPieceColor
    for row in range (pieceRows):
        for col in range(pieceCols):
            curRow = startRow + row
            curCol = startCol + col
            if(data.fallingPieceShape[row][col] == True):
                data.fallenPiece[curRow][curCol][0] = True
                data.fallenPiece[curRow][curCol][1] = color

def drawFallenPiece(canvas, data):
    rows = len(data.fallenPiece)
    cols = len(data.fallenPiece[0])
    for row in range(rows):
        for col in range(cols):
            if data.fallenPiece[row][col][0] == True:
                color = data.fallenPiece[row][col][1]
                drawCell(canvas, data, row, col, color)



def drawFallingPiece(canvas, data):
    pieceRows = len(data.fallingPieceShape)
    pieceCols = len(data.fallingPieceShape[0])
    for row in range (pieceRows):
        for col in range(pieceCols):
            if data.fallingPieceShape[row][col] == True:
                color = data.fallingPieceColor
                drawCell(canvas,data,data.fallingPieceRow+row,
                            data.fallingPieceCol + col,color)

def moveFallingPiece(data, drow, dcol):
    data.fallingPieceRow += drow
    data.fallingPieceCol += dcol
    pieceWidth = len(data.fallingPieceShape[0])
    pieceHeight = len(data.fallingPieceShape)

    if not isLegalMove(data):
        data.fallingPieceRow -= drow
        data.fallingPieceCol -= dcol          
        return False
    return True

def isLegalMove(data):
    pieceWidth = len(data.fallingPieceShape[0])
    pieceHeight = len(data.fallingPieceShape)
    startRow = data.fallingPieceRow
    startCol = data.fallingPieceCol
    for row in range(pieceHeight):
        for col in range(pieceWidth):
            (curRow,curCol) = (startRow + row, startCol + col)
            if ((curRow < 0) or (curCol < 0) or (curCol >= data.cols) or
                (curRow >= data.rows) or 
                ((data.fallenPiece[curRow][curCol][0] == True) and 
                    data.fallingPieceShape[row][col] == True)):
                return False
    return True



def rotateFallingPiece(data):
    oldRows = len(data.fallingPieceShape)
    oldCols = len(data.fallingPieceShape[0])
    oldLocRow = data.fallingPieceRow
    oldLocCol = data.fallingPieceCol
    oldList = data.fallingPieceShape
    (newCols,newRows) = (oldRows,oldCols)
    newList = [[0]*oldRows for row in range(oldCols)]
    newLocRow = round(oldLocRow + oldRows/2 - newRows/2)
    newLocCol = round(oldLocCol + oldCols/2 - newCols/2)
    newPieceWidth = len(newList[0])
    newPieceHeight = len(newList)
    for oldRow in range(oldRows):
        for oldCol in range(oldCols):
            newList[oldCols-1-oldCol][oldRow] = oldList[oldRow][oldCol]

    if ( (newLocCol >= 0) and (newLocRow >= 0) and 
        ((newPieceHeight + newLocRow - 1) < data.rows) and
        ((newPieceWidth + newLocCol - 1) < data.cols) ):
                data.fallingPieceShape = copy.deepcopy(newList)
                data.fallingPieceCol = newLocCol
                data.fallingPieceRow = newLocRow

def drawBoard(canvas, data):
    # draw grid of cells
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas, data, row, col,data.board[row][col])

def drawCell(canvas, data, row, col, color):
    (x0, y0, x1, y1) = getCellBounds(row, col, data)
    m = 1 # cell outline margin
    canvas.create_rectangle(x0, y0, x1, y1, fill="black")
    canvas.create_rectangle(x0+m, y0+m, x1-m, y1-m, fill=color)


def drawGame(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="orange")
    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)
    drawFallenPiece(canvas,data)
    if data.isGameOver == True:
        drawGameOver(canvas,data)
    removeFullRows(data)
    drawScore(canvas,data)

def drawScore(canvas,data):
    canvas.create_text(data.width/2,data.margin + 5,
        text = "Scores: %d" % (data.scores), anchor = S, fill = "black", 
        font = "Helvetica 15 bold")

def redrawAll(canvas, data):
    drawGame(canvas, data)


def drawGameOver(canvas,data):
    rectangleCenterY = 0.5 * data.height
    rectangleCenterX = 0.5 * data.width
    recWidth = 0.8 * data.width
    recHeight = 1/6 * data.height
    canvas.create_rectangle(rectangleCenterX - 0.5 * recWidth,
        rectangleCenterY - 0.5 * recHeight,rectangleCenterX + 0.5 * recWidth,
        rectangleCenterY + 0.5 * recHeight, fill = "yellow", width = 3)
    canvas.create_text(rectangleCenterX,rectangleCenterY,text = "Game Over",
        fill = "red", font = "Helvetica 26 bold")
    
def removeFullRows(data):
    currentScore = 0
    for row in range(data.rows):
        if allTrue(data,row) == True:
            moveFallenPiece(data,row)
            currentScore += 1
    data.scores += currentScore ** 2

def allTrue(data,row):
    cols = len(data.fallenPiece[0])
    for col in range(cols):
        if data.fallenPiece[row][col][0] == False:
            return False
    return True

def moveFallenPiece(data,deleteRow):
    rows = len(data.fallenPiece)
    cols = len(data.fallenPiece[0])
    emptyList = []
    for col in range(cols):
        emptyList.append([False, None])

    for row in range(rows-1,-1,-1):
        if row <= deleteRow and row!=0:
            temp = copy.deepcopy(data.fallenPiece[row-1])
            data.fallenPiece[row] = copy.deepcopy(temp)
        elif row == 0:
            data.fallenPiece[0] = copy.deepcopy(emptyList)













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

####################################
# playTetris() [calls run()]
####################################

def playTetris():
    rows = 15
    cols = 10
    margin = 20 # margin around grid
    cellSize = 20 # width and height of each cell
    width = 2*margin + cols*cellSize
    height = 2*margin + rows*cellSize
    run(width, height)

playTetris()





####################################
# testFunction 
####################################

class StructTest(object): pass
data2 = StructTest()
def init(data2):
    data2.cols = 15
    data2.rows = 10
    rowList = []
    data2.fallenPiece = []
    for row in range(data2.rows):
        colList = []
        for col in range(data2.cols):
            colList.append([False,None])
            rowList.append(colList)
    data2.fallenPiece = copy.deepcopy(rowList)


def testRemoveFullRows(data2):
    print("Testing allTrue()...", end = '')
    data2.fallenPiece[0][0][0] = True
    assert(allTrue(data2,0) == False)
    data2.fallenPiece[0][0] = [  [True,"red"],[True,"red"],[True,"red"],
                                [True,"red"],[True,"red"],[True,"red"],
                                [True,"red"],[True,"red"],[True,"red"],
                                [True,"red"]
                            ]
    assert(allTrue(data2,0) == False)
    print("passed")


def testAll():
    
 
    
    init(data2)
    testRemoveFullRows(data2)

testAll()