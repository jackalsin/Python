# hw10

# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import random

class Plane(object):
    """the bottom Plane"""
    def __init__(self, x,y,size):
        self.x = x # up 
        self.y = y # mid
        self.size = size
        self.color = "green"
        self.baseColor = "maroon"
        self.LTX = self.x - self.size/2 
        self.RBX = self.x + self.size/2
        self.LTY = self.y + 0.25 * self.size
        self.RBY = self.y + 2/3*self.size 
        self.step = 5

    def drawSelf(self,canvas):
        (x,y,size) = (self.x,self.y,self.size)
        canvas.create_polygon(x,y,x-1/3*size,y+2/3*size,x+1/3*size,y+2/3*size,
                        width = 0, fill = self.color)
        self.LTX = self.x - self.size/2 
        self.RBX = self.x + self.size/2
        self.LTY = self.y + 0.25 * self.size
        self.RBY = self.y + 2/3*self.size 
        LTX = self.LTX
        RBX = self.RBX
        LTY = self.LTY
        RBY = self.RBY
        canvas.create_rectangle(LTX,LTY,RBX,RBY, width = 0,fill=self.baseColor)

    def getArea(self):
        return (self.LTX,self.LTY,self.RBX, self.RBY)



class Barricade(object):
    """docstring for Barricades"""
    def __init__(self, width, height, cx, cy):
        self.cx = cx
        self.cy = cy
        self.width = width
        self.height = height
        self.colors = ["black","pink","indian red", "brown", "red"]
        self.HP = 4 # 0 is dead

    def drawSelf(self,canvas):
        upOffset = self.height/2
        leftOffset = self.width/2
        (cx,cy) = (self.cx,self.cy)
        canvas.create_rectangle(cx-leftOffset,cy-upOffset,
                cx+leftOffset,cy+upOffset,fill = self.colors[self.HP])

        
    def HPdown(self):
        self.HP -= 1

    def getArea(self):
        upOffset = self.height/2
        leftOffset = self.width/2
        (cx,cy) = (self.cx,self.cy)
        return (cx-leftOffset,cy-upOffset,cx+leftOffset,cy+upOffset)


class Monster(object):
    """docstring for Monster, the basic top cyan"""
    def __init__(self, x,y,row,col,data):
        self.x = x 
        self.y = y
        self.r = data.MonsterSize 
        self.HP = 1
        self.stepLength = data.stepLength
        self.monsterColor = "cyan"
        self.fire = False
        self.rowNum = row
        self.colNum = col

    def move(self,stepLength):
        self.x += stepLength
        return

    def drawSelf(self,canvas):
        r = self.r
        color = self.monsterColor
        canvas.create_oval(self.x-r,self.y-r,self.x+r,self.y+r,fill = color)

    def printSelf(self):
        print("self.x = %d y = %d fire = %r Row = %d Col = %d" % (self.x,self.y,self.fire,self.rowNum,self.colNum))

# end of Monster Definition


class MonsterB(Monster):
    """docstring for MonsterB"""
    def __init__(self, x,y,row,col,data):
        super().__init__(x,y,row,col,data)
        self.monsterColor = "deep pink"
        
class MonsterC(Monster):
    """docstring for MonsterC"""
    def __init__(self, x,y,row,col,data):
        super().__init__(x,y,row,col,data)
        self.monsterColor = "yellow"
        
def initBars(data):
    total = (data.barNum * data.Barwidth + 
                    (data.barNum - 1) * (data.barOffset - data.Barwidth))
    (startX,startY) =(data.width/2 - total/2 + data.Barwidth/2,data.barY)
    for i in range(data.barNum):
        cx = startX + i * data.barOffset
        data.barList.append(Barricade(data.Barwidth, data.BarHeight,
                                             cx, data.barY))

def drawBars(canvas,data):
    for bar in data.barList:
        bar.drawSelf(canvas)


def initMonster(data): 
    initMonsterCorX(data)
    initMonsterA(data)
    initMonsterB(data)
    initMonsterC(data)

def initMonsterCorX(data):
    startX = data.width/2 - (data.MCols - 1) * data.MOffset/2
    for i in range(data.MCols):
        x = startX + i * data.MOffset
        data.MonsterCorX.append(x)

def initMonsterA(data):
    startY = (-(1+(data.MBrows + data.MCrows - 2) + 1)*data.MOffset + 
                                                    data.width-200)
    for row in range (data.MArows):
        temp = []
        for col in range(data.MCols):
            cx = data.MonsterCorX[col]
            cy = startY + row * data.MOffset
            temp.append(Monster(cx,cy,data.monsterRows,col,data))
        data.monsterRows+=1
        data.MonsterAList.append(temp)

def drawMonsterA(canvas,data):
    (rows, cols) = (len(data.MonsterAList), len(data.MonsterAList[0]))
    for row in range(rows):
        for col in range(cols):
            data.MonsterAList[row][col].drawSelf(canvas)

def initMonsterB(data):
    startY = -((data.MCrows-1) + 1 + 1)*data.MOffset + data.width-200
    for row in range (data.MBrows):
        temp = []
        for col in range(data.MCols):
            cx = data.MonsterCorX[col]
            cy = startY + row * data.MOffset
            temp.append(MonsterB(cx,cy,data.monsterRows, col,data))
        data.monsterRows += 1
        data.MonsterBList.append(temp)
    return

def drawMonsterB(canvas,data):
    (rows, cols) = (len(data.MonsterBList), len(data.MonsterBList[0]))
    for row in range(rows):
        for col in range(len(data.MonsterBList[row])):
            data.MonsterBList[row][col].drawSelf(canvas)

def initMonsterC(data):
    startY = -(1)*data.MOffset + data.width-200
    for row in range (data.MCrows):
        temp = []
        for col in range(data.MCols):
            cx = data.MonsterCorX[col]
            cy = startY + row * data.MOffset
            temp.append(MonsterC(cx,cy,data.monsterRows, col,data))
        data.monsterRows += 1
        data.MonsterCList.append(temp)

def drawMonsterC(canvas,data):
    (rows, cols) = (len(data.MonsterCList), len(data.MonsterCList[0]))
    for row in range(rows):
        for col in range(len(data.MonsterCList[row])):
            data.MonsterCList[row][col].drawSelf(canvas)


def drawMonster(canvas,data):
    drawMonsterA(canvas,data)
    drawMonsterB(canvas,data)
    drawMonsterC(canvas,data)


class Bullet(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 1
        self.v = 5
        self.color = "blue"

    def drawSelf(self,canvas):
        (x,y,r) = (self.x,self.y,self.size)
        canvas.create_oval(x-r,y-r,x+r,y+r, width=0, fill = self.color)

    def move(self):
        self.y -= self.v


class MonsterBullet(Bullet):
    """docstring for monsterBullet"""
    def __init__(self,x,y):
        super().__init__(x,y)
        self.color = "orchid"
        
    def move(self):
        self.y += self.v

def drawBullets(canvas,data):
    for bullet in data.bullets:
        bullet.drawSelf(canvas)

def initFireTable(data):
    rows = len(data.MonsterCList)
    for col in range(len(data.MonsterCList[rows - 1])):
        data.MonsterCList[rows-1][col].fire = True



####################################
# customize these functions
####################################

def init(data):
    # game control
    data.pause = False
    data.lost = False

    # canvas
    data.height = 800
    data.width = 800
#   # canvas

    # plane 
    (data.planeX,data.planeY,data.size) = (data.width/2, data.height - 50, 50)
    data.plane = Plane(data.planeX,data.planeY,data.size)

    # brrricades 
    (data.Barwidth,data.BarHeight) = (50,30)
    data.barList = []
    data.barNum = 4
    data.barOffset = 100
    data.barY = data.height -150 # need adjust
    initBars(data)

    # Monsters
    data.MCols = 10 # for all monster
    data.monsterRows = 0 # label to init monsters
    data.MOffset = 50
    data.MonsterCorX =[]
    data.MonsterSize = 10
    data.stepLength = 10 

    # monster A
    data.MArows = 1
    data.MonsterAList = []


    # Monster B
    data.MBrows = 2
    data.MonsterBList = []

    # Monster C
    data.MCrows = 2
    data.MonsterCList = []
    # Monster Init
    initMonster(data)

    # bullets
    data.bullets = []


    data.timeFireCounter = 1
    data.STEPS = 12
    data.stepCounter = data.STEPS
    data.stepDirect = 1
    data.stepLength = 5

    # monster Firetable
    initFireTable(data)


    data.monsterBullets=[]

    data.winFlag = False

    data.finalScore = 0



def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    if event.keysym =='R' or event.keysym =='r':
        init(data)
        return
    if event.keysym == "Left":
        data.plane.x -= data.plane.step
    elif event.keysym == "Right":
        data.plane.x += data.plane.step
    elif event.keysym == "Up":
        (px,py) = (data.plane.x,data.plane.y)
        temp = Bullet(px,py)
        data.bullets.append(temp)

def checkWin(data):
    for row in data.MonsterAList:
        for MonsterA in row:
            return False
    for row in data.MonsterBList:
        for MonsterB in row:
             return False
    for row in data.MonsterCList:
        for MonsterC in row:
            return False
    data.winFlag = True
    return True

def timerFired(data):

    if data.pause == True: return
    # move bullets 
    for bullet in data.bullets:
        if bullet.y <= 0: data.bullets.remove(bullet)
        bullet.move()
        # barraide
        for bar in data.barList:
            (barX1,barY1,barX2,barY2) = bar.getArea()
            if ((barX1<=bullet.x <=barX2) and (barY1<=bullet.y<=barY2)):
                data.bullets.remove(bullet)
                bar.HPdown()
        # check enemy hit
        trueHit = checkMonster(data, bullet.x,bullet.y) 
        if trueHit: data.bullets.remove(bullet)
    # check bar
    for bar in data.barList:
        if bar.HP == 0:
            data.barList.remove(bar)

    # move monster
    if data.timeFireCounter == 1:
        # first time enter
        data.stepCounter -= 2
        moveMonster(data,data.stepLength)
        if data.stepCounter == 0:
            data.stepCounter=data.STEPS
            data.timeFireCounter = 0
            data.stepDirect = (-1)*data.stepDirect
    else:
        data.stepCounter-=1
        stepLength = data.stepDirect * data.stepLength
        moveMonster(data,stepLength)
        if data.stepCounter == 0:
            data.stepCounter=data.STEPS
            data.stepDirect = (-1)*data.stepDirect


    # monster Fire
    chooseMonsterFire(data)
    for bullet in data.monsterBullets:
        if bullet.y <= 0: data.monsterBullets.remove(bullet)
        bullet.move()

    checkMonsterBulletHitPlane(data)
    checkMonsterBulletHitBar(data)

    if checkWin(data) == True:
        data.pause == True

def setFireLable(data,bulletRow,bulletCol):
    for row in data.MonsterAList:
        for MonsterA in row:
            if ((MonsterA.rowNum == bulletRow) and 
                    (MonsterA.colNum == bulletCol)):
                    MonsterA.fire = True


    for row in data.MonsterBList:
        for MonsterB in row:
            if ((MonsterB.rowNum == bulletRow) and 
                    (MonsterB.colNum == bulletCol)):
                    MonsterB.fire = True



    for row in data.MonsterCList:
        for MonsterC in row:
            if ((MonsterC.rowNum == bulletRow) and 
                    (MonsterC.colNum == bulletCol)):
                    MonsterC.fire = True

    ## 

def display(data):   
    for row in data.MonsterAList:
        if len(row) != 0:
            for MonsterA in row:
                MonsterA.printSelf()
    for row in data.MonsterBList:
        if len(row) != 0:
            for MonsterB in row:
                MonsterB.printSelf()
    for row in data.MonsterCList:
        if len(row) != 0:
            for MonsterC in row:
                MonsterC.printSelf()



def checkMonsterBulletHitBar(data):
    for bullet in data.monsterBullets:
        if bullet.y <= 0: data.monsterBullets.remove(bullet)
        bullet.move()
        # barraide
        for bar in data.barList:
            (barX1,barY1,barX2,barY2) = bar.getArea()
            if ((barX1<=bullet.x <=barX2) and (barY1<=bullet.y<=barY2)):
                data.monsterBullets.remove(bullet)
                bar.HPdown()
    # check bar
    for bar in data.barList:
        if bar.HP == 0:
            data.barList.remove(bar)

def checkMonsterBulletHitPlane(data):
    (LTX,LTY,RBX, RBY) = data.plane.getArea()
    for bullet in data.monsterBullets:
        if ((LTX<=bullet.x<=RBX) and (LTY<=bullet.y<=RBY)):
            data.pause = True
            data.lost = True

def gameLost(canvas,data):
    canvas.create_text(data.width/2,data.height/2,text = " YOU LOSE",font="Helvetica 26 bold underline")


def drawMonsterBullets(canvas,data):
    for bullet in data.monsterBullets:
        bullet.drawSelf(canvas)

def chooseMonsterFire(data):
    tgtRow = random.randint(0,4)
    tgtCol = random.randint(0,9)
    for row in data.MonsterAList:
        for MonsterA in row:
            if ((MonsterA.rowNum == tgtRow) and (MonsterA.colNum == tgtCol) and MonsterA.fire == True):
                temp = MonsterBullet(MonsterA.x,MonsterA.y + MonsterA.r)
                data.monsterBullets.append(temp)

    for row in data.MonsterBList:
        for MonsterB in row:
            if ((MonsterB.rowNum == tgtRow) and (MonsterB.colNum == tgtCol) and MonsterB.fire == True):
                temp = MonsterBullet(MonsterB.x,MonsterA.y + MonsterB.r)
                data.monsterBullets.append(temp)
    for row in data.MonsterCList:
        for MonsterC in row:
            if ((MonsterC.rowNum == tgtRow) and (MonsterC.colNum == tgtCol) and MonsterC.fire == True):
                temp = MonsterBullet(MonsterC.x,MonsterC.y + MonsterC.r)
                data.monsterBullets.append(temp)


def moveMonster(data,stepLength):
    for row in data.MonsterCList:
        if len(row) != 0:
            for MonsterC in row:
                MonsterC.move(stepLength)
    for row in data.MonsterBList:
        if len(row) != 0:
            for MonsterB in row:
                MonsterB.move(stepLength)
    for row in data.MonsterAList:
        if len(row) != 0:
            for MonsterA in row:
                MonsterA.move(stepLength)

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def checkMonster(data, x,y):
    for row in data.MonsterAList:
        if len(row) != 0:
            for MonsterA in row:
                if distance(x,y,MonsterA.x,MonsterA.y) <= MonsterA.r:
                    (monsterRow,monsterCol) = (MonsterA.rowNum, MonsterA.colNum)
                    if (monsterRow != 0): 
                        setFireLable(data,monsterRow-1,monsterCol)
                    data.finalScore += 100
                    row.remove(MonsterA)
                    return True
    for row in data.MonsterBList:
        if len(row) != 0:
            for MonsterB in row:
                if distance(x,y,MonsterB.x,MonsterB.y) <= MonsterB.r:
                    (monsterRow,monsterCol) = (MonsterB.rowNum, MonsterB.colNum)
                    if (monsterRow != 0): 
                        setFireLable(data,monsterRow-1,monsterCol)
                    data.finalScore += 100
                    row.remove(MonsterB)
                    return True
    for row in data.MonsterCList:
        if len(row) != 0:
            for MonsterC in row:
                if distance(x,y,MonsterC.x,MonsterC.y) <= MonsterC.r:
                    (monsterRow,monsterCol) = (MonsterC.rowNum, MonsterC.colNum)
                    if (monsterRow != 0): 
                        setFireLable(data,monsterRow-1,monsterCol)
                    data.finalScore += 100
                    row.remove(MonsterC)
                    return True
    return False

def drwaInstruction(canvas,data):
    canvas.create_text(data.width/2, 50,anchor = N, 
            text = "UP: Fire || Left/Right Arrow: move|| presss r to restart")

def redrawAll(canvas, data):
    drwaInstruction(canvas,data)
    data.plane.drawSelf(canvas)
    drawBars(canvas,data)
    drawMonster(canvas,data)
    drawBullets(canvas,data)
    drawMonsterBullets(canvas,data)
    if data.winFlag == True:
        displayWin(canvas,data)
        return
    if data.lost == True: 
        gameLost(canvas,data)
        return
    pass
def displayWin(canvas,data):
    canvas.create_text(data.width/2,data.height/2,text = " YOU LOSE",
                                    font="Helvetica 26 bold underline")
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

run(400,400)


class OopyInvaders(object):
    totalGamesPlayed = 0 

    def __init__(self,data):
        init(data)
        finalScore = 0
        totalGamesPlayed += 1

    @staticmethod
    def run():
        run()

    def getTheFinalScore(self,data = data):
        return