# drawMaps
import pygame, configure,random,tiles
class Maps(object):
    """docstring for Maps"""
    def __init__(self,rows = None, cols = None):
        self.c = configure.Configure()
        if (rows == None or cols == None):
            self.rows = self.c.ROWS
            self.cols = self.c.COLS
        else:
            self.rows = rows
            self.cols = cols

        self.generateMaps(self.rows, self.cols)

        self.board = [] # map is digits, but board have tiles
        self.initBoard()

    def generateMaps(self,rows, cols):
        self.map = [[None] * cols for row in range(rows)]
        for row in range(rows):
            for col in range (cols):
                if (row == 0 or col == 0 or col == (cols - 1) or (row == rows - 1)):
                    self.map[row][col] = self.c.WALL # create the bondray wall
                elif (row % 2 == 0 and col % 2 == 0): # generate the wall
                    self.map[row][col] = self.c.WALL
                else:
                    if (random.randint(0,100) < 15):
                        self.map[row][col] = self.c.BRICK # create the ground
                    else:
                        self.map[row][col] = self.c.GROUND
        # outside the loop: 
        # 1. clear init position 
        # 2. deploy powerup, Bombup, lifeup, timeup
        
        # 2. deploy powerup, Bombup, lifeup, timeup
        specialPowerList = [self.c.BOMB_UP,self.c.POWER_UP,self.c.LIFE_UP,self.c.TIME_UP]
        for i in range(len(specialPowerList)):
            row, col = self.generateValid()
            self.map[row][col] = specialPowerList[i]            
        

        # Now clearing the left top corner 
        self.map[1][1] = self.map[1][2] = self.map[2][1] = self.c.GROUND
        # Now clearing the right top corner
        self.map[1][cols-2]=self.map[2][cols-2] = self.map[1][cols-2] = self.c.GROUND


    def generateValid(self):
        rows = self.rows
        cols = self.cols
        while True:
            row = random.randint(0,rows - 1)
            col = random.randint(0,cols - 1)
            if self.map[row][col] == self.c.GROUND:
                return (row,col)

    def initBoard(self):
        rows = self.rows
        cols = self.cols
        for row in range(rows):
            temp = []
            for col in range(cols):
                temp.append(tiles.Tile(self.map[row][col])) # add obj to board
            self.board.append(temp)                


    def getTile(self,position):
        # on Nov 26, row should be 1, col should be 0

        row = position[1]//self.c.TILE_SIZE
        col = position[0]//self.c.TILE_SIZE
        return (self.board[row][col])


# ------- test only ---------- #

    def printMap(self):
        rows = self.rows
        cols = self.cols
        for i in range(rows):
            print("[",end = "")
            for j in range(cols):
                print(self.map[i][j],end =", ")
            print("]")
