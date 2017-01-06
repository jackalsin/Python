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

        ######### Graphic Value
        self.x = None
        self.y = None

    def drawSelf(self,canvas):
        if self.gateType == "input":
            drawInput(canvas,self.x,self.y,self.inputValues)
        elif self.gateType == "output":
            drawOutput(canvas,self.x,self.y)
        elif self.gateType == "not":
            drawNot(canvas,self.x,self.y)
        elif self.gateType == "or":
            drawOr(canvas,self.x,self.y)
        elif self.gateType == "and":
            drawAnd(canvas,self.x,self.y)
        else:
            print("drawSelf function is down")

    def connectTo(self,outputObj):
        self.outputGates.append(outputObj)
        self.maxOutputGates += 1
        outputObj.inputGates.append(self)
        outputObj.maxInputGates += 1

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
        # print(self.inputValues)
        if self.inputValues[None] == True:
            self.outputValue = True
        elif self.inputValues[None] == False:
            self.outputValue = False
        # print("we are exiting do_in")


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
class Wire(object):
    def __init__ (self,startIndex,startX,startY,endX,endY):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.status = False # True for on, False for off
        self.colors = ["red", "black"]
        self.startIndex = startIndex

    def drawSelf(canvas,self):
        if self.status == False:
            color = self.colors[1]
        else:
            color = self.colors[0]
        canvas.create_line(self.startX,self.startY,self.endX,self.endY, 
            fill = color)

def init(data):
    # load data.xyz as appropriate
    # Graphic Data
    data.upperMargin = 50
    data.menuSize = 100
    
    data.innerBound = 5 

    data.buttonHeight = 30 
    data.buttonWidth = 70
    data.buttonXStart = 150
    data.buttonYStart = data.upperMargin/2 - data.buttonHeight/2
  
    data.buttonInterval = 40
    data.textMargin = 5
    data.menuMargin = 10

    data.drawType = None # as a flag

    data.components = [] # 
    data.drawTypeMapping=["not","or","and","input","output"]


    data.wires = []
    data.connectFlag = False
    (data.wireX1,data.wireY1,data.wireX2,
        data.wireY2)=(None,None,None,None) # temp value to mark wire
    data.startIndex = None
    data.endIndex = None

    data.validR = 10

    data.powerFlag = False
    pass

def mousePressed(event, data):
    # left menu
    if 0<=event.x<=data.menuSize and (data.upperMargin<=event.y<data.height):
        if data.drawType == None:
            i = (event.y - data.upperMargin)//100
            data.drawType = i
    # effective canvas
    elif event.x > data.menuSize and (data.upperMargin<=event.y<data.height):
        if type(data.drawType)==int:
            print("we not Flag the %d" % (data.drawType))
            temp = Gate(data.drawTypeMapping[data.drawType])
            temp.y = min(max(event.y,data.upperMargin+data.menuSize/2),
                            data.height-data.menuSize/2) # ensure in the canvas
            if data.drawType in [0,1,2]:
                temp.x = event.x
            elif data.drawType == 3:
                temp.x = data.menuSize+data.innerBound
            elif data.drawType == 4:
                temp.x = data.width - data.innerBound
            data.components.append(temp)
            data.drawType = None

        elif data.drawType == None and data.powerFlag==False: # try to connect, didn't click the menu
            (startIndex,startX,startY)=isValidConnectClick(data,event.x,event.y)
            # startIndex should be int, not exist equals False
            if startIndex != None and data.connectFlag==False:
                data.wireX1 = startX
                data.wireY1 = startY
                data.startIndex = startIndex
                data.connectFlag = True

            elif startIndex != None and data.connectFlag == True: #second Valid
                data.wireX2 = startX
                data.wireY2 = startY
                data.endIndex = startIndex
                data.connectFlag = False

            if None not in [data.wireX1,data.wireY2]: # value set,create obj
                print("",data.startIndex,data.endIndex,data.wireX1,data.wireY1)
                (data.startIndex,data.endIndex) = indexCalibrate(data)
                temp = Wire(data.startIndex,data.wireX1,data.wireY1,
                                                    data.wireX2,data.wireY2)
                data.wires.append(temp)
                
                startObj = data.components[data.startIndex]
                endObj = data.components[data.endIndex]
                startObj.connectTo(endObj)
                (data.startIndex,data.endIndex,data.wireX1,data.wireY1,     
                    data.wireX2,data.wireY2)=(None,None,None,None,None,None)

        elif data.powerFlag == True:
            print("enter the powerFlag True")
            (componentIndex,centerX,centerY) = isValidConnectClick(data,event.x,
                                                                    event.y)
            selectedObj=data.components[componentIndex] 
            if selectedObj.gateType=="input":
                # set Value
                print(selectedObj.inputValues)
                if selectedObj.inputValues == None:
                    value = True
                else:
                    value = not selectedObj.inputValues[None]
                selectedObj.setInputValue(None,value)
                # update wire state
                 # put it in the timeFire? when power on update
            else:
                print("Not a valid click in power on mode")
    # Upper Button zone
    else:
        if (((data.upperMargin-data.buttonHeight)/2)<=event.y<=(
                        (data.upperMargin+data.buttonHeight)/2)):
            L0 = data.buttonXStart
            width = data.buttonWidth
            interval = data.buttonInterval
            bias = width+interval
            if ((L0)<=event.x<=(L0+width)):
                do_clear(data)
            elif((L0+bias)<=event.x<=(L0+width+bias)):
                # do_load(data)
                return
            elif ((L0+2*bias)<=event.x<=(L0+width+bias*2)):
                # do_save(data)
                return
            elif ((L0+3*bias)<=event.x<=(L0+width+bias*3)):
                data.powerFlag = not data.powerFlag
                return

def updateWireState(data):
    # print("updating updateWireState")
    for wire in data.wires:
        startComp = data.components[wire.startIndex]
        wire.status = startComp.outputValue

def indexCalibrate(data):
    startIndex = data.startIndex
    endIndex = data.endIndex
    startObj = data.components[startIndex]
    endObj = data.components[endIndex]
    if endObj.gateType == "input":
        print("end input swap")
        return(endIndex,startIndex)
    elif startObj.gateType == "output":
        print('output swap')
        return(endIndex,startIndex)
    # elif data.wireX1 > startObj.x: # startobj should be output,which is greater
    #     print(data.wireX1,startObj.x)
    #     print("smaller")
    #     return(startIndex,endIndex)
    # else:
    #     print("we perform the swap")
    #     return(endIndex,startIndex)

    return (startIndex,endIndex)

def isValidConnectClick(data,x,y):
    for componentIndex in range(len(data.components)):
        if data.components[componentIndex].gateType == "input":
            comp = data.components[componentIndex]
            (validX,validY) =(comp.x, comp.y)
            if distance(x,y,comp.x,comp.y)<data.validR:
                return (componentIndex,comp.x,comp.y)
            
        elif data.components[componentIndex].gateType == "output":
            comp = data.components[componentIndex]
            (validX,validY) =(comp.x, comp.y)
            if distance(x,y,comp.x,comp.y)<data.validR:
                return (componentIndex,comp.x,comp.y)
            
        elif data.components[componentIndex].gateType == "not":
            # print("enter the not")
            comp = data.components[componentIndex]
            (in1x,in1y)=(comp.x-50+15,comp.y-50+50)
            (out1x,out1y) = (comp.x-50+90,comp.y-50+50)
            # print("print distance",distance(in1x,in1y,x,y),distance(out1x,out1y,x,y))
            if distance(in1x,in1y,x,y)<data.validR:
                return(componentIndex,in1x,in1y)
            elif distance(out1x,out1y,x,y)<data.validR:
                return(componentIndex,out1x,out1y)
            
        elif data.components[componentIndex].gateType == "or":
            comp = data.components[componentIndex]
            (in1x,in1y)=(comp.x-50+20,comp.y-50+42)
            (in2x,in2y)=(comp.x-50+20,comp.y-50+58)
            (out1x,out1y) = (comp.x-50+70,comp.y-50+50)
            if distance(in1x,in1y,x,y)<data.validR:
                return(componentIndex,in1x,in1y)
            elif distance(in2x,in2y,x,y)<data.validR:
                return(componentIndex,in2x,in2y)
            elif distance(out1x,out1y,x,y)<data.validR:
                return(componentIndex,out1x,out1y)
            else:
                print("Or is wrong")

        elif data.components[componentIndex].gateType == 'and':

            comp = data.components[componentIndex]
            (in1x,in1y)=(comp.x-50+20,comp.y-50+42)
            (in2x,in2y)=(comp.x-50+20,comp.y-50+58)
            (out1x,out1y) = (comp.x-50+80,comp.y-50+50)
            if distance(in1x,in1y,x,y)<data.validR:
                return(componentIndex,in1x,in1y)
            elif distance(in2x,in2y,x,y)<data.validR:
                return(componentIndex,in2x,in2y)
            elif distance(out1x,out1y,x,y)<data.validR:
                print("distance ok, return")
                return(componentIndex,out1x,out1y)
            else:
                print("and is wrong")
        else:
            print("something wrong in isValidConnectClick")
    
    return (None,None,None)
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    if data.powerFlag == True:
        updateWireState(data)
    else:
        for wire in data.wires:
            wire.status = False
    pass

def redrawAll(canvas, data):
    drawInterFace(canvas,data)
    drawInnerBound(canvas,data) # Left and right line
    drawComponents(canvas,data)
    drawWire(canvas,data)

    pass

def drawWire(canvas,data):
    for wire in data.wires:
        (x1,y1,x2,y2) = (wire.startX,wire.startY,wire.endX,wire.endY)
        if wire.status == False or wire.status == None:
            color = wire.colors[1] # black
        else:
            color = wire.colors[0] # red
        canvas.create_line(x1,y1,x2,y2,fill = color)


def do_clear(data):
    data.components=[]
    data.wires=[]


def drawInnerBound(canvas,data):
    endX = startX = data.menuSize+data.innerBound
    startY = data.upperMargin
    endY = data.height
    canvas.create_line(startX,startY,endX,endY,fill = "blue")
    endX = startX = data.width - data.innerBound
    canvas.create_line(startX,startY,endX,endY,fill = "blue")


def drawComponents(canvas,data):
    for comp in data.components:
        comp.drawSelf(canvas)


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
        if i == 3:
            if data.powerFlag == False:
                buttonText[i] = "power off"
            else:
                buttonText[i] = "power on"
        canvas.create_text((LTx+RBx)/2,(RBy+LTy)/2,
            text = buttonText[i], font="Times 12 bold")

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


def drawInput(canvas,midX,midY,state = None):
    rOut = 8
    rIn = 5

    canvas.create_oval(midX-rOut,midY-rOut,midX+rOut,midY+rOut,fill = "purple")
    if state == None:
        canvas.create_oval(midX-rIn,midY-rIn,midX+rIn,midY+rIn,fill = "black")
    else:
        if state[None] == False:
            canvas.create_oval(midX-rIn,midY-rIn,midX+rIn,midY+rIn,
                                                                fill = "black")
        else:
            canvas.create_oval(midX-rIn,midY-rIn,midX+rIn,midY+rIn,fill = "red")

    
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
