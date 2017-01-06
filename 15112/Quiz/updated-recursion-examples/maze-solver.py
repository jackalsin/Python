# mazeSolver.py

from tkinter import *
import random
import math

NORTH = (-1,0)
SOUTH = (1,0)
EAST  = (0,1)
WEST  = (0,-1)

def keyPressed(event, data):
    row,col = data.playerSpot
    if data.inHelpScreen:
        data.inHelpScreen = False
    elif event.char=="+":
        init(data, data.rows+1, data.cols+1, False)
    elif event.char=="-":
        init(data, data.rows-1, data.cols-1, False)
    elif event.char=="h":
        data.inHelpScreen = True
    elif event.char=="r":
        resetGame(data)
    elif event.char=="c":
        data.isPolar = not data.isPolar
    elif event.char=="s":
        #toggle solution
        if data.solution==None:
            data.solution = solveMaze(data)
        else:
            data.solution=None
    elif event.keysym == "Up" and isValid(data, row,col,NORTH):
        doMove(data, row,col,NORTH)
    elif event.keysym == "Down" and isValid(data, row,col,SOUTH):
        doMove(data, row,col,SOUTH)
    elif event.keysym == "Left" and isValid(data, row,col,WEST):
        doMove(data, row,col,WEST)
    elif event.keysym == "Right" and isValid(data, row,col,EAST):
        doMove(data, row,col,EAST)

def resetGame(data):
    rows,cols = len(data.maze),len(data.maze[0])
    data.solution = None
    data.path = set([(0,0)])
    data.playerSpot = (0,0)
    data.maze = makeBlankMaze(rows,cols)
    connectIslands(data.maze)

def isValid(data, row,col,direction):
    maze = data.maze
    rows,cols = len(maze),len(maze[0])
    if not (0<=row<rows and 0<=col<cols): return False
    if direction==EAST: return maze[row][col].east
    if direction==SOUTH: return maze[row][col].south
    if direction==WEST: return maze[row][col-1].east
    if direction==NORTH: return maze[row-1][col].south
    assert False

def doMove(data, row,col,direction):
    (drow,dcol) = direction
    maze,path = data.maze,data.path
    rows,cols = len(maze),len(maze[0])
    if not (0<=row<rows and 0<=col<cols): return False
    if ((row+drow,col+dcol)) in path: path.remove((row,col))
    else: path.add((row+drow,col+dcol))
    data.playerSpot = (row+drow,col+dcol)

def solveMaze(data):
    maze = data.maze
    rows,cols = len(maze),len(maze[0])
    visited = set()
    targetRow,targetCol = rows-1,cols-1
    def solve(row,col):
        # base cases
        if (row,col) in visited: return False
        visited.add((row,col))
        if (row,col)==(targetRow,targetCol): return True
        # recursive case
        for drow,dcol in [NORTH,SOUTH,EAST,WEST]:
            if isValid(data, row,col,(drow,dcol)):
                if solve(row+drow,col+dcol): return True
        visited.remove((row,col))
        return False
    return visited if solve(0,0) else None

##################################### draw #####################################

def redrawAll(canvas, data):
    if data.inHelpScreen: return drawHelpScreen(canvas, data)
    canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
    drawBridges(canvas, data)
    drawIslands(canvas, data)
    if data.solution!=None: drawSolutionPath(canvas, data, data.solution)
    drawPlayerPath(canvas, data)

def drawHelpScreen(canvas, data):
    font = "Helvetica 32 bold"
    canvas.create_text(300, 50, text="Maze Solver", font=font)
    font = "Helvetica 24 bold"
    messages = [
                "arrows to solve manually",
                "r to reset (make new maze)",
                "s to toggle solution on/off",
                "c to toggle circular (polar) on/off",
                "+ to increase maze size",
                "- to decrease maze size",
                "h to view this help screen",
                "press any key to continue"
                ]
    for i in range(len(messages)):
        canvas.create_text(300, 150+50*i, text=messages[i], font=font)

def drawIslands(canvas, data):
    islands = data.maze
    rows,cols = len(islands),len(islands[0])
    color = data.islandColor
    r = min(data.cW,data.cH)/6
    for row in range(rows):
        for col in range(cols):
            drawCircle(canvas, islandCenter(data, row,col),r,color)

def drawCircle(canvas, position, r, color):
    (cx,cy) = position
    canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=color,width=0)

def islandCenter(data, row, col):
    if data.isPolar:
        cx,cy = data.width/2,data.height/2
        rows,cols = len(data.maze),len(data.maze[0])
        maxR = min(cx,cy)
        r = maxR*(row+1)/(rows+1)
        theta = 2*math.pi*col/cols
        return cx+r*math.cos(theta), cy-r*math.sin(theta)
    else:
        cellWidth,cellHeight = data.cW,data.cH
        return (col+0.5)*cellWidth,(row+0.5)*cellHeight

def drawBridges(canvas, data):
    islands = data.maze
    rows,cols = len(islands),len(islands[0])
    color = data.bridgeColor
    width = min(data.cW,data.cH)/15
    for r in range(rows):
        for c in range(cols):
            island = islands[r][c]
            if (island.east):
                canvas.create_line(islandCenter(data, r,c),
                                   islandCenter(data, r,c+1),
                                   fill=color, width=width)
            if (island.south):
                canvas.create_line(islandCenter(data, r,c),
                                   islandCenter(data, r+1,c),
                                   fill=color, width=width)

def drawPlayerPath(canvas, data):
    path = data.path
    (pRow,pCol) = data.playerSpot
    color = data.pathColor
    r = min(data.cW,data.cH)/6
    width = min(data.cW,data.cH)/15
    for (row,col) in path:
        drawCircle(canvas, islandCenter(data, row,col),r,color)
        if (row+1,col) in path and isValid(data, row,col,SOUTH):
            canvas.create_line(islandCenter(data, row,col),
                                   islandCenter(data, row+1,col),
                                   fill=color, width=width)
        if (row,col+1) in path and isValid(data, row,col,EAST):
            canvas.create_line(islandCenter(data, row,col),
                                   islandCenter(data, row,col+1),
                                   fill=color, width=width)
    drawCircle(canvas, islandCenter(data, pRow,pCol),r,data.playerColor)
    
def drawSolutionPath(canvas, data, path):
    color = data.solutionColor
    r = min(data.cW,data.cH)/6
    width = min(data.cW,data.cH)/15
    for (row,col) in path:
        drawCircle(canvas, islandCenter(data, row,col),r,color)
        if (row+1,col) in path and isValid(data, row,col,SOUTH):
            canvas.create_line(islandCenter(data, row,col),
                                   islandCenter(data, row+1,col),
                                   fill=color, width=width)
        if (row,col+1) in path and isValid(data, row,col,EAST):
            canvas.create_line(islandCenter(data, row,col),
                                   islandCenter(data, row,col+1),
                                   fill=color, width=width)

##################################### init #####################################

def init(data, rows=10, cols=10, inHelpScreen=True):
    if (rows < 1): rows = 1
    if (cols < 1): cols = 1
    data.inHelpScreen = inHelpScreen
    data.rows = rows
    data.cols = cols
    data.islandColor = "dark green"
    data.bridgeColor = "white"
    data.pathColor = "blue"
    data.playerColor = "green"
    data.solutionColor = "red"
    data.isPolar = False
    data.path = set()
    data.solution = None
    data.playerSpot = (0,0)
    data.path.add(data.playerSpot)
    margin = 5
    data.cW = (data.width - margin)/cols
    data.cH = (data.height - margin)/rows
    data.margin = margin
    #make the islands
    data.maze = makeBlankMaze(rows,cols)
    #connect the islands
    connectIslands(data.maze)

class Struct(object): pass

def makeIsland(number):
    island = Struct()
    island.east = island.south = False
    island.number = number
    return island

def makeBlankMaze(rows,cols):
    islands = [[0]*cols for row in range(rows)]
    counter = 0
    for row in range(rows):
        for col in range(cols):
            islands[row][col] = makeIsland(counter)
            counter+=1
    return islands

def connectIslands(islands):
    rows,cols = len(islands),len(islands[0])
    for i in range(rows*cols-1):
        makeBridge(islands)

def makeBridge(islands):
    rows,cols = len(islands),len(islands[0])
    while True:
        row,col = random.randint(0,rows-1),random.randint(0,cols-1)
        start = islands[row][col]
        if flipCoin(): #try to go east
            if col==cols-1: continue
            target = islands[row][col+1]
            if start.number==target.number: continue
            #the bridge is valid, so 1. connect them and 2. rename them
            start.east = True
            renameIslands(start,target,islands)
        else: #try to go south
            if row==rows-1: continue
            target = islands[row+1][col]
            if start.number==target.number: continue
            #the bridge is valid, so 1. connect them and 2. rename them
            start.south = True
            renameIslands(start,target,islands)
        #only got here if a bridge was made
        return

def renameIslands(i1,i2,islands):
    n1,n2 = i1.number,i2.number
    lo,hi = min(n1,n2),max(n1,n2)
    for row in islands:
        for island in row:
            if island.number==hi: island.number=lo

def flipCoin():
    return random.choice([True, False])

def mousePressed(event, data): pass

def timerFired(data): pass

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

run(600, 600)