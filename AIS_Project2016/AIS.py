# mode-demo.py

from tkinter import *

####################################
# init
####################################

def init(data):
    # There is only one init, not one-per-mode
    data.mode = "startScreen"
    data.color1 = "green"
    data.color2 = "green"
    data.color3 = "green"
    data.color4 = "red"
##############4##########4##########
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "startScreen"): startScreenMousePressed(event, data)
    elif (data.mode == "choiceScreen"):   choiceScreenMousePressed(event, data)
    elif (data.mode == "checkOccupany"):       checkOccupanyMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "startScreen"): startScreenKeyPressed(event, data)
    elif (data.mode == "choiceScreen"):   choiceScreenKeyPressed(event, data)
    elif (data.mode == "checkOccupany"):       checkOccupanyKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "startScreen"): startScreenTimerFired(data)
    elif (data.mode == "choiceScreen"):   choiceScreenTimerFired(data)
    elif (data.mode == "checkOccupany"):       checkOccupanyTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "startScreen"): startScreenRedrawAll(canvas, data)
    elif (data.mode == "choiceScreen"):   choiceScreenRedrawAll(canvas, data)
    elif (data.mode == "checkOccupany"):       checkOccupanyRedrawAll(canvas, data)

####################################
# startScreen mode
####################################

def startScreenMousePressed(event, data):
    pass

def startScreenKeyPressed(event, data):
    data.mode = "choiceScreen"

def startScreenTimerFired(data):
    pass

def startScreenRedrawAll(canvas, data):
    canvas.create_rectangle( 0, 0, 1000, 600, fill="red",
                                                outline="black", width=3)
    canvas.create_rectangle( 100, 100, 900, 500, fill="white",
                                                outline="black", width=3)
    canvas.create_text(data.width/2, data.height/2-100,
                       text="Carnegie Mellon University Hunt Library!", font="Arial 40 bold")
    canvas.create_rectangle( 300, 300, 700, 350, fill="green",
                                                outline="black", width=3)
    canvas.create_text(data.width/2, data.height/2+20,
                       text="find a seat now( press any key to continue)", font="Arial 20")

####################################
# choiceScreen mode
####################################

def choiceScreenMousePressed(event, data):
    if event.x > 200 and event.x<300 and event.y>300 and event.y<380:
        data.mode = "checkOccupany"
    elif event.x > 350 and event.x<450 and event.y>300 and event.y<380:
        data.mode = "checkOccupany"
    elif event.x > 500 and event.x<600 and event.y>300 and event.y<380:
        data.mode = "checkOccupany"
    elif event.x > 650 and event.x<750 and event.y>300 and event.y<380:
        data.mode = "checkOccupany"

def choiceScreenKeyPressed(event, data):
    pass

def choiceScreenTimerFired(data):
    pass

def choiceScreenRedrawAll(canvas, data):
    canvas.create_rectangle( 0, 0, 1000, 600, fill="red",
                                                outline="black", width=3)
    canvas.create_rectangle( 100, 100, 900, 500, fill="white",
                                                outline="black", width=3)
    canvas.create_text(250, 150,
                       text="choice the floor", font="Arial 40 bold")
    canvas.create_rectangle( 200, 300, 300, 380, fill="white",
                                                outline="black", width=3)
    canvas.create_rectangle( 350, 300, 450, 380, fill="white",
                                                outline="black", width=3)
    canvas.create_rectangle( 500, 300, 600, 380, fill="white",
                                                outline="black", width=3)
    canvas.create_rectangle( 650, 300, 750, 380, fill="white",
                                                outline="black", width=3)
    canvas.create_text(250, 340,
                       text="floor1", font="Arial 20 bold")
    canvas.create_text(400, 340,
                       text="floor2", font="Arial 20 bold")
    canvas.create_text(550,340,
                       text="floor3", font="Arial 20 bold")
    canvas.create_text(700, 340,
                       text="floor4", font="Arial 20 bold")

####################################
# checkOccupany mode
####################################

def checkOccupanyMousePressed(event, data):
    pass

def checkOccupanyKeyPressed(event, data):
    pass

def checkOccupanyTimerFired(data):
    pass

def checkOccupanyRedrawAll(canvas, data):
    
    canvas.create_rectangle( 0, 0, 1000, 600, fill="red",
                                                outline="black", width=3)
    canvas.create_rectangle( 100, 100, 900, 500, fill="white",
                                                outline="black", width=3)
    canvas.create_text(200, 150,
                       text="Occupany", font="Arial 40 bold")
    canvas.create_rectangle( 200, 300, 300, 380, fill=data.color1,
                                                outline="black", width=3)
    canvas.create_rectangle( 350, 300, 450, 380, fill=data.color2,
                                                outline="black", width=3)
    canvas.create_rectangle( 500, 300, 600, 380, fill=data.color3,
                                                outline="black", width=3)
    canvas.create_rectangle( 650, 300, 750, 380, fill=data.color4,
                                                outline="black", width=3)
    canvas.create_text(250, 340,
                       text="seat1", font="Arial 20 bold")
    canvas.create_text(400, 340,
                       text="seat2", font="Arial 20 bold")
    canvas.create_text(550,340,
                       text="seat3", font="Arial 20 bold")
    canvas.create_text(700, 340,
                       text="seat4", font="Arial 20 bold")


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

run(1000, 600)