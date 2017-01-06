from Tkinter import *

import math
from PIL import Image, ImageTk
from tkSimpleDialog import askinteger


class DrawingCanvas(Canvas):
    def __init__(self, p, w, h, bg):
        # type: (object, object, object, object) -> object
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
        length = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) * 0.1

        self.create_line(x2, y2, x2 - length, y2 - length, width=self.globalLineWidth, fill=self.globalAnnotationColor)
        self.create_line(x2, y2, x2 - length, y2 + length, width=self.globalLineWidth, fill=self.globalAnnotationColor)
        return self.create_line(x1, y1, x2, y2, width=self.globalLineWidth, fill=self.globalAnnotationColor)

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
        r = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return self.create_oval((x1 - r, y1 - r), (x1 + r, y1 + r))

    def DrawImage(self, filename):
        if (self.currentDrawingImage > 0):
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

    def changeAnnotColor(self, color):
        globalAnnotationColor = color

    def ChangeAnnotationColor(self):
        top = Toplevel
        top.title("Choose the annotation color")
        msg = Message(top, text="please choose a color for annotations: ")
        msg.pack()
        button1 = Button(top, text="Red", command=self.changeAnnotColor("red"))
        button2 = Button(top, text="Blue", command=self.changeAnnotColor("blue"))
        button3 = Button(top, text="Green", command=self.changeAnnotColor("green"))
        button4 = Button(top, text="Yellow", command=self.changeAnnotColor("yellow"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

# root = Tk()
# canvas = DrawingCanvas(root, 500, 500, "white")
# canvas.pack()
# root.mainloop()
#
# canvas.DrawCircle()
# canvas.DrawArrow()