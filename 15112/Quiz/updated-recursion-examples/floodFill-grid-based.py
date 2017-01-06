# FloodFill using Tkinter
# grid-based (not pixel-based), with animation
# and numeric display of depth of recursion
# also, this version is based on our barebones animation code
# Actually, adapted from grid-demo.py

from tkinter import *

class Cell(object):
    def __init__(self):
        self.depth = self.ordinal = -1 # set by floodFill
        self.displayLabel = False
        self.isWall = False

def make2dList(rows, cols):
    a=[]
    for row in range(rows): a += [[0]*cols]
    return a

def init(data):
    data.rows = 4
    data.cols = 6
    data.margin = 5 # margin around grid
    data.cells = make2dList(data.rows, data.cols)
    data.gridSize = min(data.width, data.height)
    for row in range(data.rows):
        for col in range(data.cols):
            data.cells[row][col] = Cell()
    data.floodFillIndex = 0
    data.displayOrdinals = False

def pointInGrid(x, y, data):
    # return True if (x, y) is inside the grid defined by data.
    return ((data.margin <= x <= data.width-data.margin) and
            (data.margin <= y <= data.height-data.margin))

def getCell(x, y, data):
    # aka "viewToModel"
    # return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
    if (not pointInGrid(x, y, data)):
        return (-1, -1)
    gridWidth  = data.gridSize - 2*data.margin
    gridHeight = data.gridSize - 2*data.margin
    cellWidth  = gridWidth / data.cols
    cellHeight = gridHeight / data.rows
    row = int((y - data.margin) / cellHeight)
    col = int((x - data.margin) / cellWidth)
    # triple-check that we are in bounds
    row = min(data.rows-1, max(0, row))
    col = min(data.cols-1, max(0, col))
    return (row, col)

def getCellBounds(row, col, data):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = data.gridSize - 2*data.margin
    gridHeight = data.gridSize - 2*data.margin
    x0 = data.margin + gridWidth * col / data.cols
    x1 = data.margin + gridWidth * (col+1) / data.cols
    y0 = data.margin + gridHeight * row / data.rows
    y1 = data.margin + gridHeight * (row+1) / data.rows
    return (x0, y0, x1, y1)

def clearLabels(data):
    for row in range(data.rows):
        for col in range(data.cols):
            cell = data.cells[row][col]
            cell.depth = cell.ordinal = -1
    data.floodFillOrder = [ ]
    data.floodFillIndex = 0
    data.displayOrdinals = False

def floodFill(data, row, col, depth=0):
    if ((row < 0) or (row >= data.rows) or
        (col < 0) or (col >= data.cols)):
        return # off-board!
    cell = data.cells[row][col]
    if (cell.isWall == True):
        return # hit a wall
    if (cell.depth >= 0):
        return # already been here

    # "fill" this cell
    cell.depth = depth
    cell.ordinal = len(data.floodFillOrder)
    data.floodFillOrder.append(cell)

    # then recursively fill its neighbors
    floodFill(data, row-1, col,   depth+1)
    floodFill(data, row+1, col,   depth+1)
    floodFill(data, row,   col-1, depth+1)
    floodFill(data, row,   col+1, depth+1)

def mousePressed(event, data):
    clearLabels(data)
    (row, col) = getCell(event.x, event.y, data)
    shift = ((event.state & 0x0001) != 0)
    if (shift == False):
        data.cells[row][col].isWall = not data.cells[row][col].isWall
    else:
        data.cells[row][col].isWall = False
        floodFill(data, row, col)

def keyPressed(event, data):
    if (event.keysym == "d"):
        data.displayOrdinals = False
    elif (event.keysym == "o"):
        data.displayOrdinals = True
    elif (event.keysym == "r"):
        init(data)

def timerFired(data):
    data.floodFillIndex += 1

def redrawAll(canvas, data):
    # draw grid of cells
    for row in range(data.rows):
        for col in range(data.cols):
            (x0, y0, x1, y1) = getCellBounds(row, col, data)
            cell = data.cells[row][col]
            fill = "pink" if (cell.isWall) else "cyan"
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)
            if ((cell.depth >= 0) and
                (cell.ordinal < data.floodFillIndex)):
                (cx, cy) = ((x0+x1)/2, (y0+y1)/2)
                if (data.displayOrdinals == True):
                    label = "# " + str(cell.ordinal)
                else:
                    label = str(cell.depth)
                canvas.create_text(cx, cy, text=label,
                                   font="Arial 12 bold", fill="darkGreen")
    drawHelpText(canvas, data)

def drawHelpText(canvas, data):
    messages = [
                "Click to toggle walls",
                "Shift-click to floodFill from cell",
                "Press 'd' to display depths",
                "Press 'o' to display #ordinals",
                "Press 'r' to reset"
               ]
    dTextY = 20
    for i in range(len(messages)):
        canvas.create_text(data.width/2, data.gridSize + (i+1)*dTextY,
                           text=messages[i],
                           font="Arial 18 bold", fill="darkBlue")

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

run(300, 420)