# Name Zhiwei Xin
# Andrew ID: zxin
# Homework 8a 

class Gate(object):
    def __init__(self, typeString):
        self.gateType = typeString #"input","output"
        self.outputGates = []
        self.inputGates =[]
        self.maxInputGates = 0
        self.maxOutputGates = 0
        
        self.inputValues = None
        self.outputValue = None



    def connectTo(self,outputObj):
        self.outputGates.append(outputObj)
        self.maxOutputGates += 1
        outputObj.inputGates.append(self)
        outputObj.maxInputGates +=1

    def getMaxInputGates(self):
        return self.maxInputGates

    def getMaxOutputGates(self):
        return self.maxOutputGates

    def getInputGates(self):
        return self.inputGates

    def getOutputGates(self):
        return self.outputGates

    def input2output(self):
        # make input 2 output value
        if self.gateType == "input":
            self.do_in()
        elif self.gateType == "output":
            self.do_out()
        elif self.gateType == "not":
            self.do_not()
        elif self.gateType == "and":
            self.do_and()
        elif self.gateType == "or":
            self.do_or()
        elif self.gateType == "xor":
            self.do_xor()
        else: 
            print("evaluation wrong")

        if self.maxOutputGates != 0: # do determine is None, Len() now work
            for outputGate in self.getOutputGates(): 
                outputGate.input2output()

    def do_in(self):
        print(self.inputValues)
        if self.inputValues[None] == True:
            self.outputValue = True
        elif self.inputValues[None] == False:
            self.outputValue = False
        print("we are exiting do_in")


    def do_out(self):
        self.inputValues = dict()
        for inputGate in self.inputGates:
            self.inputValues[inputGate] = inputGate.outputValue

        # actually only one

        if self.inputValues[inputGate] == True:
            self.outputValue = True
        else:
            self.outputValue = False

    def do_not(self):
        self.inputValues = dict()
        inputGate = self.inputGates[0]
        self.inputValues[inputGate] = inputGate.outputValue

        # signal evaluation
        if self.inputValues[inputGate] == True:
            self.outputValue = False
        else:
            self.outputValue = True


    def do_and(self):
        self.inputValues = dict()
        for inputGate in self.inputGates:
            if inputGate.outputValue != None:
                self.inputValues[inputGate] = inputGate.outputValue
        # Evaluation

        if len(self.inputValues) < 2:
            self.outputValue = None
        else:
            booleanValueList = []
            for inputGate in self.inputValues:
                booleanValueList.append(self.inputValues[inputGate])
            if False in booleanValueList:
                self.outputValue = False
            else:
                self.outputValue = True

    def do_or(self):
        self.inputValues = dict()
        for inputGate in self.inputGates:
            if inputGate.outputValue != None:
                self.inputValues[inputGate] = inputGate.outputValue
        # Evaluation

        if len(self.inputValues) < 2:
            self.outputValue = None
        else:
            booleanValueList = []
            for inputGate in self.inputValues:
                booleanValueList.append(self.inputValues[inputGate])
            if True in booleanValueList:
                self.outputValue = True
            else:
                self.outputValue = False
      

    def setInputValue(self, key, value): # only used to initialize 
        self.inputValues = dict()
        self.inputValues[key] = value
        self.input2output()
    

def testGateClass1_inputToOutput():
    # Connect and input gate to an output gate
    in1 = Gate("input")
    out1 = Gate("output")
    in1.connectTo(out1);
    assert(in1.getInputGates() == [ ])
    assert(in1.getMaxInputGates() == 0)
    assert(in1.getOutputGates() == [ out1 ])
    assert(out1.getInputGates() == [ in1 ])
    assert(out1.getMaxInputGates() == 1)
    assert(out1.getOutputGates() == [ ])
    assert(in1.inputValues == None)
    assert(in1.outputValue == None)
    assert(out1.inputValues == None)
    assert(out1.outputValue == None)


    # now set the input to True
    in1.setInputValue(None, True)
    assert(in1.inputValues == { None:True})
    assert(in1.outputValue == True)
    assert(out1.inputValues == { in1:True})
    assert(out1.outputValue == True)
    # and set the input to False



    in1.setInputValue(None, False)
    assert(in1.inputValues == { None:False})
    assert(in1.outputValue == False)
    assert(out1.inputValues == { in1:False})
    assert(out1.outputValue == False)

def testGateClass2_oneNotGate():
    in1 = Gate("input")
    out1 = Gate("output")
    not1 = Gate("not")
    in1.connectTo(not1)
    not1.connectTo(out1)
    assert(out1.outputValue == None)
    in1.setInputValue(None, False)
    assert(not1.inputValues == { in1:False })
    assert(out1.inputValues == { not1:True })
    assert(out1.outputValue == True)
    in1.setInputValue(None, True)
    assert(not1.inputValues == { in1:True })
    assert(out1.inputValues == { not1:False })
    assert(out1.outputValue == False)

def testGateClass3_oneAndGate():
    in1 = Gate("input")
    in2 = Gate("input")
    out1 = Gate("output")
    and1 = Gate("and")
    in1.connectTo(and1)
    in2.connectTo(and1)
    and1.connectTo(out1)
    assert(out1.outputValue == None)
    in1.setInputValue(None, False)



    assert(and1.inputValues == { in1:False })
    assert(and1.outputValue == None) # not ready, need both inputs
    in2.setInputValue(None, False)
    assert(and1.inputValues == { in1:False, in2:False })
    assert(and1.outputValue == False)
    assert(out1.outputValue == False)

    in1.setInputValue(None, True)
    assert(and1.inputValues == { in1:True, in2:False })
    assert(out1.outputValue == False)

    in2.setInputValue(None, True)
    assert(and1.inputValues == { in1:True, in2:True })
    assert(out1.outputValue == True)

def testGateClass4_oneOrGate():
    in1 = Gate("input")
    in2 = Gate("input")
    out1 = Gate("output")
    or1 = Gate("or")
    in1.connectTo(or1)
    in2.connectTo(or1)
    or1.connectTo(out1)
    assert(out1.outputValue == None)
    in1.setInputValue(None, False)
    assert(or1.inputValues == { in1:False })
    assert(or1.outputValue == None) # not ready, need both inputs
    in2.setInputValue(None, False)
    assert(or1.inputValues == { in1:False, in2:False })
    assert(or1.outputValue == False)
    assert(out1.outputValue == False)

    in1.setInputValue(None, True)
    assert(or1.inputValues == { in1:True, in2:False })
    assert(out1.outputValue == True)

    in2.setInputValue(None, True)
    assert(or1.inputValues == { in1:True, in2:True })
    assert(out1.outputValue == True)

def testGateClass5_xor():
    in1 = Gate("input")
    in2 = Gate("input")
    out1 = Gate("output")
    and1 = Gate("and")
    and2 = Gate("and")
    not1 = Gate("not")
    not2 = Gate("not")
    or1 = Gate("or")
    in1.connectTo(and1)
    in1.connectTo(not1)
    in2.connectTo(and2)
    in2.connectTo(not2)
    not1.connectTo(and2)
    not2.connectTo(and1)
    and1.connectTo(or1)
    and2.connectTo(or1)
    or1.connectTo(out1)

    in1.setInputValue(None, False)
    in2.setInputValue(None, False)
    assert(out1.outputValue == False)

    in1.setInputValue(None, True)
    in2.setInputValue(None, False)
    assert(out1.outputValue == True)

    in1.setInputValue(None, False)
    in2.setInputValue(None, True)
    assert(out1.outputValue == True)

    in1.setInputValue(None, True)
    in2.setInputValue(None, True)
    assert(out1.outputValue == False)

def testGateClass():
    print("Testing Gate class... ", end="")
    testGateClass1_inputToOutput()
    testGateClass2_oneNotGate()
    testGateClass3_oneAndGate()
    testGateClass4_oneOrGate()
    testGateClass5_xor()
    print("Passed!")


testGateClass()

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################


# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    # Graphic Data
    data.upperMargin = 50
    data.menuSize = 100

    data.buttonHeight = 30 
    data.buttonWidth = 50
    data.buttonXStart = 150
    data.buttonYStart = data.upperMargin/2 - data.buttonHeight/2
  
    data.buttonInterval = 40
    data.textMargin = 5
    data.menuMargin = 10

    data.drawType = None # as a flag

    data.component = [] # 
    data.drawTypeMapping=["not","or","and","input","output"]
    pass

def mousePressed(event, data):
    if 0<=event.x<=100:
        if data.drawType == None:
            i = (event.y - data.upperMargin)//50
            data.drawType = i
    elif event.x > 100:
        if type(data.drawType)==int:
            temp = Gate(data.drawTypeMapping[data.drawType])
            data.components.append(Gate(event.x,event.y))
            data.drawType = None
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    drawInterFace(canvas,data)

    pass
def drawInterFace(canvas,data):
    canvas.create_rectangle(0,data.upperMargin,data.width,data.height)
    # draw Left
    textList = ["NOT Gate", "OR Gate","AND Gate","Input","Output"]
    for i in range (5):
        LTx = 0
        LTy = data.upperMargin + data.menuSize*i
        RBx = LTx + data.menuSize
        RBy = LTy + data.menuSize
        canvas.create_rectangle(LTx,LTy,RBx,RBy)
        canvas.create_text(LTx + data.textMargin,RBy - data.textMargin,
            text = textList[i], anchor=SW, font="Times 12 bold ")
    drawButton(canvas,data) # draw UpperButton

    # draw Left
    LTx = 0
    LTy = data.upperMargin
    RBx = LTx + data.menuSize
    RBy = LTy + data.menuSize
    midX = 0.5*(LTx+RBx)
    midY = 0.5*(LTy+RBy)
    drawNot(canvas,midX,midY)
    midY+=data.menuSize
    drawOr(canvas,midX,midY)
    midY+=data.menuSize
    drawAnd(canvas,midX,midY)
    midY+=data.menuSize
    drawInput(canvas,midX,midY)
    midY+=data.menuSize
    drawOutput(canvas,midX,midY)
    return

def drawButton(canvas,data): # upperBotton
    buttonText = ["clear", "load", "save","power"]
    for i in range(4):
        LTx = data.buttonXStart + i*(data.buttonWidth+data.buttonInterval)
        LTy = data.buttonYStart
        RBx = LTx + data.buttonWidth
        RBy = LTy + data.buttonHeight
        canvas.create_rectangle(LTx,LTy,RBx,RBy)
        canvas.create_text((LTx+RBx)/2,(RBy+LTy)/2,
            text = buttonText[i], font="Times 12 bold ")

def drawNot(canvas,x,y): # x y are the center point
    startX = x - 50
    startY = y - 50
    # draw Triangle
    canvas.create_line(startX+30,startY+30,startX+70,startY+50)
    canvas.create_line(startX+70,startY+50,startX+30,startY+70)
    canvas.create_line(startX+30,startY+30,startX+30,startY+70)

    # input
    canvas.create_line(startX+15,startY+50,startX+30,startY+50,fill = "green")

    # output
    r = 5
    canvas.create_oval(startX+70,startY+50-r,startX+70+2*r,startY+50+r)
    # draw outputLine, length = 2r
    canvas.create_line(startX+70+2*r,startY+50,startX+70+2*r+2*r,startY+50,
                                        fill = "red")
    return

def drawOr(canvas,x,y):
    startX = x - 50
    startY = y - 50
    canvas.create_polygon(startX+30,startY+30,startX+50,startY+30,
                startX+60,startY+50,startX+50,startY+70,startX+30,
                startY+70,fill = "gray")
     # output
    canvas.create_line(startX+60,startY+50,startX+70,startY+50,fill = "red") 
    # input
    canvas.create_line(startX+20,startY+42,startX+30,startY+42,fill = "green")
    canvas.create_line(startX+20,startY+58,startX+30,startY+58,fill = "green")
    return

def drawAnd(canvas,x,y):
    startX = x - 50
    startY = y - 50
    canvas.create_rectangle(startX+30,startY+30,startX+70,startY+70)

     # output
    canvas.create_line(startX+70,startY+50,startX+80,startY+50,fill = "red") 
    # input
    canvas.create_line(startX+20,startY+42,startX+30,startY+42,fill = "green")
    canvas.create_line(startX+20,startY+58,startX+30,startY+58,fill = "green")
    return


def drawInput(canvas,midX,midY):
    rOut = 8
    rIn = 5

    canvas.create_oval(midX-rOut,midY-rOut,midX+rOut,midY+rOut,fill = "red")
    canvas.create_oval(midX-rIn,midY-rIn,midX+rIn,midY+rIn,fill = "black")
    return

def drawOutput(canvas,midX,midY):
    rOut = 8
    rIn = 5

    canvas.create_oval(midX-rOut,midY-rOut,midX+rOut,midY+rOut,fill = "green")
    canvas.create_oval(midX-rIn,midY-rIn,midX+rIn,midY+rIn,fill = "black")
    return

####################################
# use the run function as-is
####################################

def run(width=1000, height=1100):
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

run(700, 550)
