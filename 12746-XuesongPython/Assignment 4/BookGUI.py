from Tkinter import *
import tkMessageBox
from BookClass import Book


class Panel(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        aCupOfJava = Book(1001, "A cup of Java", "Kumar", 44.14, 31)
        javaForDummy = Book(1002, "Java for dummies", "Tan Ah Teck", 34.12, 10)
        javaTutorial = Book(1003, "Java tutorial", "Pine Liu", 129.31, 100)
        self.books = [aCupOfJava, javaForDummy, javaTutorial]

        # run init
        self.init()

    def init(self):
        self.leftBox = Listbox(self.parent)
        self.leftBox.bind("<<ListboxSelect>>", self.boxSelectUpdate)
        self.leftBox.grid(rowspan=10, row=0, column=0)
        for book in self.books:
            self.leftBox.insert(END, book.title)
        self.setDetailPanel()

    def boxSelectUpdate(self, event):
        index = (self.leftBox.curselection()[0])
        curBook = self.books[index]
        self.updateDetailPanel(curBook)

    def updateDetailPanel(self, book):
        self.titleVariable.set(book.title)
        self.authorVariable.set(book.author)
        self.priceVariable.set(book.price)
        self.pageVariable.set(book.pages)

    def setDetailPanel(self):
        self.titleVariable = StringVar()
        self.titleEntry = Entry(self.parent, textvariable=self.titleVariable)
        self.titleEntry.grid(row=0, column=1)

        self.authorVariable = StringVar()
        self.authorEntry = Entry(self.parent, textvariable=self.authorVariable)
        self.authorEntry.grid(row=1, column=1)

        self.priceVariable = DoubleVar()
        self.priceEntry = Entry(self.parent, textvariable=self.priceVariable)
        self.priceEntry.grid(row=2, column=1)

        self.pageVariable = IntVar()
        self.pageEntry = Entry(self.parent, textvariable=self.pageVariable)
        self.pageEntry.grid(row=3, column=1)

        self.updateButton = Button(self.parent, text="Update", command=self.buttonUpdate)
        self.updateButton.grid()
        self.updateButton.grid(row=4, column=1)

    def buttonUpdate(self):
        if self.leftBox.curselection():
            index = (self.leftBox.curselection()[0])
            curBook = self.books[index]
            if self.checkInputValid():
                curBook.title = self.titleVariable.get()
                curBook.author = self.authorVariable.get()
                curBook.price = self.priceVariable.get()
                curBook.pages = self.pageVariable.get()
            else:
                print "Not update"
                tkMessageBox.showinfo("ERROR", "Cannot be empty")
        else:
            tkMessageBox.showinfo("ERROR", "No entry is selected")

    def checkInputValid(self):
        return self.titleVariable.get() and self.authorVariable.get() and self.priceVariable.get() and \
               self.pageVariable.get()


def main():
    root = Tk()
    mainPanel = Panel(root)
    root.geometry('600x600+200+100')
    root.mainloop()


if __name__ == '__main__':
    main()
