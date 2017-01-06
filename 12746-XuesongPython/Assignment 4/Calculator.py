from Tkinter import *
import tkMessageBox

class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initVal= "0"
        self.init()

    def init(self):
        self.expressionVariable = StringVar()
        self.expressionEntry = Entry(self.parent, textvariable=self.expressionVariable)
        self.expressionEntry.grid(row=0, column=0, columnspan=4)
        self.initButtonPanel()
        pass

    def initButtonPanel(self):
        listVal = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", "C", "=", "+"]
        for i in xrange (len(listVal)):
            row = i / 4
            col = i - row * 4
            button = CalButton(self.parent, listVal[i])
            button.grid(row=row + 1, column=col)
            if button.val == "C":
                button.bind("<Button-1>", self.clearButtonEvent)
            elif button.val == "=":
                button.bind("<Button-1>", self.equalButtonEvent)
            else:
                button.bind("<Button-1>", lambda event, arg=button: self.calInput(event, arg))

    def equalButtonEvent(self, event):
        try:
            expr = self.expressionVariable.get()
            self.expressionVariable.set(eval(expr))
        except Exception:
            self.expressionVariable.set("Error: invalid expression")

    def clearButtonEvent(self,event):
        self.expressionVariable.set("")

    def calInput(self, event, button):
        self.expressionVariable.set(self.expressionVariable.get() + button.val)

class CalButton(Button):
    def __init__(self, parent, val):
        Button.__init__(self, parent, text=val)
        self.val = val


def main():
    root = Tk()
    mainPanel = Calculator(root)
    root.geometry('200x200+200+100')
    root.mainloop()


if __name__ == '__main__':
    main()
