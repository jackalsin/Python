# This class defines a window object
from Tkinter import *
from DrawingClassExample import Drawing
from tkFileDialog import *
from DrawingCanvas import DrawingCanvas

class DrawingWindow():
    def __init__(self):
        self.window = Tk()
        self.drawingList = None
        self.updateButton = None
        self.labelBuildingName = None
        self.labelYearConstructed = None
        self.currentDrawing = None
        self.drawingsInfo = None
        self.drawingCanvas = None

    def newFilePressed(self):
        print 0

    def openFilePressed(self):
        drawings = []
        filepath = askopenfilename()

        if len(filepath) == 0:
            return

        f = open(filepath,"r")
        newLine = f.readline()
        index = 1
        while newLine!="":
            newLine = newLine.strip()
            parameters = newLine.split(",")
            drawings.append(Drawing(parameters[0],int(parameters[1]),parameters[2],int(parameters[3]),parameters[4],parameters[5],"Drawing #"+str(index)))

            self.drawingList.insert(END,drawings[index-1].name)

            newLine = f.readline()
            index = index+1

        self.drawingsInfo = drawings

    def saveFilePressed(self):
        print "Save file!"

    def saveAsPressed(self):
        print "Save as!"

    def updateButtonPressed(self):
        print "button clicked."
        self.labelBuildingName.config(text="New text")

    def drawLinePressed(self):
        self.drawingCanvas.drawingMode = 1

    def drawArrowPressed(self):
        self.drawingCanvas.drawingMode = 2

    def drawRectanglePressed(self):
        self.drawingCanvas.drawingMode = 3

    def drawCirclePressed(self):
        self.drawingCanvas.drawingMode = 4


    def canvasClicked(self, event):
        if self.drawingCanvas.drawingMode >0:
            if self.drawingCanvas.firstClick == None:
                self.drawingCanvas.firstClick = [event.x, event.y]
            else:
                self.drawingCanvas.secondClick = [event.x, event.y]
                self.drawingCanvas.drawComponent()

    def changeLineWidthPressed(self):
        self.drawingCanvas.changeLineWidth()

    def changeLineColorPressed(self):
        self.drawingCanvas.ChangeAnnotationColor()

    def listSelected(self,event):
        selectedIndex = self.drawingList.curselection()
        if len(selectedIndex) == 0:
            return

        drawingindex = selectedIndex[0]
        print self.drawingsInfo[drawingindex].buildingName
        self.labelBuildingName.config(text=self.drawingsInfo[drawingindex].buildingName)
        print self.drawingsInfo[drawingindex].yearConstructed
        self.labelYearConstructed.config(text=self.drawingsInfo[drawingindex].yearConstructed)
        self.drawingCanvas.DrawImage(self.drawingsInfo[drawingindex].imageFile)

    def createComponents(self):
        self.drawingList = Listbox(self.window)
        self.drawingList.grid(row=0,column=0,rowspan=3)
        self.drawingList.bind("<<ListboxSelect>>",self.listSelected)

        self.labelBuildingName = Label(self.window,text = "Building Name")
        self.labelBuildingName.grid(row=0,column=1)

        self.labelYearConstructed = Label(self.window,text = "Year Constructed")
        self.labelYearConstructed.grid(row=1,column=1)

        self.updateButton = Button(self.window,text="Update",command=self.updateButtonPressed)
        self.updateButton.grid(row=2,column=1)

        self.drawingCanvas = DrawingCanvas(self.window, 300,300,"white")
        self.drawingCanvas.grid(row = 0, column=2, rowspan = 3)
        self.drawingCanvas.bind("<Button-1>", self.canvasClicked)


    def createMenu(self):
        menubar = Menu(self.window)
        self.window.config(menu = menubar)

        fileMenu = Menu(menubar)
        menubar.add_cascade(label="File", menu=fileMenu)

        fileMenu.add_command(label="New File", command=self.newFilePressed)
        fileMenu.add_command(label="Open File", command=self.openFilePressed)
        fileMenu.add_command(label="Save File", command=self.saveFilePressed)
        fileMenu.add_command(label="Save as...", command=self.saveAsPressed)


        annotationMenu = Menu(menubar)
        menubar.add_cascade(label="Annotation", menu=annotationMenu)

        annotationMenu.add_command(label="Draw Line", command=self.drawLinePressed)
        annotationMenu.add_command(label="Draw Arrow", command=self.drawArrowPressed)
        annotationMenu.add_command(label="Draw Rectangle", command=self.drawRectanglePressed)
        annotationMenu.add_command(label="Draw Circle", command=self.drawCirclePressed)
        annotationMenu.add_separator()
        annotationMenu.add_command(label="Change Line Width", command=self.changeLineWidthPressed)
        annotationMenu.add_command(label="Change Line Color", command=self.changeLineColorPressed)

