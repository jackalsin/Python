# tetris-after-step-2.py
# fall-2015 version

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
    # pre-load a few cells with known colors for testing purposes
    data.board[0][0] = "red" # top-left is red
    data.board[0][data.cols-1] = "white" # top-right is white
    data.board[data.rows-1][0] = "green" # bottom-left is green
    data.board[data.rows-1][data.cols-1] = "gray" # bottom-right is gray


    data.paused = False

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
    data.fallenPiece = [[False] * data.cols for row in range(data.rows)]
    data.fallenPiece[14][5] = True
    print(data.fallenPiece)



def newFallingPiece(data):
    pieceShapeIndex = random.randint(0,6)
    pieceColorIndex = random.randint(0,6)
    data.fallingPieceShape = data.tetrisPieces[pieceShapeIndex]
    data.fallingPieceColor = data.tetrisPieceColors[pieceColorIndex]
    pieceLength = len(data.fallingPieceShape[0])
    data.fallingPieceCol = data.cols//2 - pieceLength//2




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
    if (event.keysym == "p"):
        data.paused = not data.paused
    elif (event.keysym == "Left"):
        moveFallingPiece(data,0,-1)
    elif (event.keysym == "Right"):
        moveFallingPiece(data, 0, 1)
    elif (event.keysym == "Down"):
        moveFallingPiece(data,1,0)
    elif (event.keysym == "Up"):
        rotateFallingPiece(data)


def timerFired(data):
    moveFallingPiece(data, 1, 0)

def drawGame(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="orange")
    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)

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
    print("we have called this function")
    data.fallingPieceRow += drow
    data.fallingPieceCol += dcol
    pieceWidth = len(data.fallingPieceShape[0])
    pieceHeight = len(data.fallingPieceShape)
    print("pieceWidth, pieceHeight", pieceWidth,pieceHeight)


    nextRow = data.fallingPieceRow + 1
    for newCol in range(pieceWidth):
        if ((nextRow == data.rows) or 
                (data.fallenPiece[nextRow][newCol] == True) or 
            data.fallingPieceCol < 0 or 
            (data.fallingPieceCol+pieceWidth-1) >= data.cols or 
            data.fallingPieceRow < 0 or 
            (data.fallingPieceRow + pieceHeight-1) >= data.rows):
            data.fallingPieceRow -= drow
            data.fallingPieceCol -= dcol          
        


    # if (data.fallingPieceCol < 0 or 
    #     (data.fallingPieceCol+pieceWidth-1) >= data.cols or 
    #     data.fallingPieceRow < 0 or 
    #     (data.fallingPieceRow + pieceHeight-1) >= data.rows): 
    #     data.fallingPieceRow -= drow
    #     data.fallingPieceCol -= dcol          
        
    # else:
    #     nextRow = data.fallingPieceRow + 1
    #     for newCol in range(pieceWidth):
    #         if ((nextRow == data.rows) or 
    #             (data.fallenPiece[nextRow][newCol] == True)):
    #             data.fallingPieceRow -= drow
    #             data.fallingPieceCol -= dcol                 


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

def placeFallingPiece(data):
    newLocRow = data.fallingPieceRow
    newLocCol = data.fallingPieceCol
    newRows = len(data.fallingPieceShape)
    newCols = len(data.fallingPieceShape[0])

    for newRow in range(newRows):
        for newCol in range(newCols):
            curRow = newLocRow + newRow
            curCol = newLocCol + newCol





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

def redrawAll(canvas, data):
    drawGame(canvas, data)





















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

# run(300, 300)

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
