# Homework 9 
# Andrew ID: zxin
# Name: Zhiwei Xin

import os
import copy

def findLargestFile(path):
    fileList = getPathList(path)
    bestFile = ""
    bestSize = 0.0
    for subFile in fileList:
        curSize = os.path.getsize(subFile)
        if bestSize < curSize:
            bestFile = subFile
            bestSize = curSize
    return bestFile

def getPathList(path):
    if (os.path.isdir(path) == False):
        return [path]
    else:
        fileList = []
        for filename in os.listdir(path):
            fileList += getPathList(path+"/"+filename)
        return fileList


def testGetPathList():
    print("testGetPathList()...",end = "")
    assert(getPathList("sampleFiles/folderA") ==
                       ['sampleFiles/folderA/fishing.txt', 
    'sampleFiles/folderA/folderC/folderD/misspelled.txt', 
    'sampleFiles/folderA/folderC/folderD/penny.txt', 
    'sampleFiles/folderA/folderC/folderE/tree.txt', 
    'sampleFiles/folderA/folderC/giftwrap.txt', 
    'sampleFiles/folderA/widths.txt'])

    print("passed.")

   
def testFindLargestFile():
    print("testFindLargestFile()...",end = "")
    assert(findLargestFile("sampleFiles/folderA") ==
                       "sampleFiles/folderA/folderC/giftwrap.txt")

    assert(findLargestFile("sampleFiles/folderB") ==
                       "sampleFiles/folderB/folderH/driving.txt")
    assert(findLargestFile("sampleFiles/folderB/folderF") == "")
    print("passed.")


def flatten(L):
    result = []
    if(type(L) != list):
        return L
    else:
        result = []
        for i in range(len(L)):
            if type(L[i]) == list:
                temp = flatten(L[i])
            else:
                temp = [L[i]]
            result+=(temp)
        return result
    

def testFlatten():
    print("testFlatten()...",end = "")
    assert(flatten([1,[2]]) == [1,2])
    assert(flatten([1,2,[3,[4,5],6],7]) == [1,2,3,4,5,6,7])
    assert(flatten(['wow', [2,[[]]], [True]]) == ['wow', 2, True])
    assert(flatten([]) == [])
    assert(flatten([[]]) == [])
    assert(flatten(3) == 3)
    print("passed.")


def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

def findRTP(digits):
    digits -= 1
    result = list()
    def isRTP(digits, guess = 2):
        if not (isPrime(guess)):
            return False
        if guess > 10**digits:
            print("guess is ", guess) 
            result.append(guess)
            return True
        for i in range(10):
            temp = guess * 10 + i
            if (isRTP(digits, temp) == False):
                continue
            else:
                return True
        return isRTP(digits,guess + 1)
    isRTP(digits)
    return result[0]


def noError(f):
    import functools
    cachedResults = dict()
    @functools.wraps(f)
    def wrapper(*args):
        try:
            return f(*args)
        except:
            return None
    return wrapper




def testNoErrorDecorator():
    print("Testing @noError decorator...", end="")
    @noError
    def f(x, y): return x/y
    assert(f(1, 5) == 1/5)
    assert(f(1, 0) == None)

    @noError
    def g(): return 1/0
    assert(g() == None)

    @noError
    def h(n):
        if (n == 0): return 1
        else: return h(n+1)
    assert(h(0) == 1)
    assert(h(-1) == 1)
    assert(h(1) == None)

    print("Passed!")



def getCourse(courseCatalog, courseNumber):
    def getCourseInner(courseCatalog,courseNumber):
        if(type(courseCatalog[0]) == str ):
            if(courseNumber in courseCatalog): return courseNumber
            else: # not in 
                if(len(courseCatalog[1:])>0): # not the end 
                    return getCourseInner(courseCatalog[1:],courseNumber)
                else: return None
        else:
            result = getCourseInner(courseCatalog[0], courseNumber)
            if (type(courseCatalog[0][0])==list): return result
            if (result != None):
                return courseCatalog[0][0] + '.' +result
            elif (len(courseCatalog) == 1): # reach the end 
                return None
            else:
                resultIn = getCourseInner(courseCatalog[1:],courseNumber)
                if(resultIn == None):return None
                else: return resultIn
    result = getCourseInner(courseCatalog,courseNumber)
    if result != None: return courseCatalog[0] + '.' + result
    else: return None 

def testGetCourse():
    print("getCourse()...",end = "")
    courseCatalog = ["CMU",
                        ["CIT",
                            [ "ECE", "18-100", "18-202", "18-213" ],
                            [ "BME", "42-101", "42-201" ],
                        ],
                        ["SCS",
                            [ "CS", 
                              ["Intro", "15-110", "15-112" ],
                              "15-122", "15-150", "15-213"
                            ],
                        ],
                        "99-307", "99-308"
                    ]

    assert(getCourse(courseCatalog, "18-100") == "CMU.CIT.ECE.18-100")
    assert(getCourse(courseCatalog, "15-112") == "CMU.SCS.CS.Intro.15-112")
    assert(getCourse(courseCatalog, "15-213") == "CMU.SCS.CS.15-213")
    assert(getCourse(courseCatalog, "99-307") == "CMU.99-307")
    assert(getCourse(courseCatalog, "15-251") == None)
    print("passed")


def testAll():
    testFindLargestFile()
    testGetPathList()
    testFlatten()
    testGetCourse()
    testNoErrorDecorator()

    
testAll()

































































######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

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

# run(800, 800)
