from Tkinter import *
from PIL import Image, ImageTk
from tkSimpleDialog import askinteger
import math


class DrawingCanvas(Canvas):
    def __init__(self, p, w, h, bg):
        Canvas.__init__(self, master=p, width=w, height=h, bg=bg)
        self.globalAnnotationColor = "red"
        self.globalLineWidth = 3
        self.currentDrawingImage = 0

        # drawingMode attribute: 0 means not drawing. 1 means draw line.
        # 2 means draw arrow. 3 means draw rectangle, 4 means draw circle
        self.drawingMode = 0

        self.firstClick = None
        self.secondClick = None

    def drawComponent(self):
        if self.drawingMode == 1:
            self.DrawLine()
        elif self.drawingMode == 2:
            self.DrawArrow()
        elif self.drawingMode == 3:
            self.DrawRectangle()
        elif self.drawingMode == 4:
            self.DrawCircle()

        self.firstClick = None
        self.secondClick = None
        self.drawingMode = 0

    def DrawLine(self):
        x1 = self.firstClick[0]
        y1 = self.firstClick[1]
        x2 = self.secondClick[0]
        y2 = self.secondClick[1]

        return self.create_line(x1, y1, x2, y2, width=self.globalLineWidth, fill=self.globalAnnotationColor)

    def DrawArrow(self):
        x1 = self.firstClick[0]
        y1 = self.firstClick[1]
        x2 = self.secondClick[0]
        y2 = self.secondClick[1]
        # Draw body
        self.create_line(x1, y1, x2, y2, width=self.globalLineWidth, fill=self.globalAnnotationColor)
        l = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 * 0.3
        theta = math.pi / 6
        alpha = self.getBodyAngle(x1, y1, x2, y2)
        upperWingX1 = x2 + l * math.cos(alpha + math.pi - theta)
        upperWingY1 = y2 + l * math.sin(alpha + math.pi - theta)

        lowerWingX1 = x2 + l * math.cos(math.pi + alpha + theta)
        lowerWingY1 = y2 + l * math.sin(math.pi + alpha + theta)

        self.create_line(upperWingX1, upperWingY1, x2, y2, width=self.globalLineWidth, fill=self.globalAnnotationColor)
        self.create_line(lowerWingX1, lowerWingY1, x2, y2, width=self.globalLineWidth, fill=self.globalAnnotationColor)

    def getBodyAngle(self, x1, y1, x2, y2):
        if x1 == x2:
            return math.pi / 2
        relativeAngle = float(math.atan(float(abs(y2 - y1)) / float(abs(x2 - x1))))
        xSign = x2 - x1
        ySign = y2 - y1
        if xSign >= 0:
            if ySign >= 0:
                return relativeAngle
            else:
                return math.pi * 2 - relativeAngle
        else:
            if ySign >= 0:
                return math.pi - relativeAngle
            else:
                return math.pi + relativeAngle

    def DrawRectangle(self):
        x1 = self.firstClick[0]
        y1 = self.firstClick[1]
        x2 = self.secondClick[0]
        y2 = self.secondClick[1]
        return self.create_rectangle(x1, y1, x2, y2, width=self.globalLineWidth, fill="",
                                     outline=self.globalAnnotationColor)

    def DrawCircle(self):

        x1 = self.firstClick[0]
        y1 = self.firstClick[1]
        x2 = self.secondClick[0]
        y2 = self.secondClick[1]
        r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        leftTopX1 = x1 - r
        leftTopY1 = y1 - r
        rightBottomX2 = x1 + r
        rightBottomY2 = y1 + r
        return self.create_oval(leftTopX1, leftTopY1, rightBottomX2, rightBottomY2, width=self.globalLineWidth, fill="",
                                outline=self.globalAnnotationColor)

    def DrawImage(self, filename):
        if self.currentDrawingImage > 0:
            self.delete(self.currentDrawingImage)

        file = Image.open(filename)
        file = file.resize((300, 300))

        image = ImageTk.PhotoImage(file)

        self.currentDrawingImage = self.create_image(0, 0, anchor=NW, image=image)
        self.image = image

    def changeLineWidth(self):
        newvalue = askinteger("New Line Width",
                              "The current line width is " + str(self.globalLineWidth) + ". Please enter new value")
        if newvalue > 0:
            self.globalLineWidth = newvalue

    def ChangeAnnotationColor(self):
        top = Toplevel()
        top.title("Choose a color")

        colorValues = ["red", "blue", "green"]

        for colorValue in colorValues:
            Radiobutton(top, text=colorValue, value=colorValue, command=lambda: self.setColor(colorValue)).pack()

    def setColor(self, color):
        self.globalAnnotationColor = color
