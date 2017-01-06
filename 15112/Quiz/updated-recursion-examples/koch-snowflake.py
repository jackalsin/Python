# koch-snowflake.py

import turtle

def kochSide(length, n):
    if (n == 1):
        turtle.forward(length)
    else:
        kochSide(length/3.0, n-1)
        turtle.left(60)
        kochSide(length/3.0, n-1)
        turtle.right(120)
        kochSide(length/3.0, n-1)
        turtle.left(60)
        kochSide(length/3.0, n-1)

def kochSnowflake(length, n):
    for step in range(3):
        kochSide(length, n)
        turtle.right(120)

turtle.delay(0)
turtle.speed(0)
turtle.penup()
turtle.goto(-300,100)
turtle.pendown()

turtle.pencolor("black")
kochSide(300, 4) # same as k4(300)

turtle.pencolor("blue")
kochSnowflake(300, 4)

turtle.penup()
turtle.goto(-250,50)
turtle.pendown()
turtle.pencolor("red")
kochSnowflake(200, 5)
turtle.done()