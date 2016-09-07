'''
This is the Assignment 1 for 12746 Assignment 1 Fall 2016
If you find this file by google in my Github, you suck!
@author Zhiwei Xin
@andrewID: zxin
'''

##!/usr/bin/python2


# print the multipllication table
def printMultilicationTableInForSquare():
    format = "%d * %d = %d, "
    for i in xrange(1, 10):
        for j in xrange(1, 10):
            print format % (i, j, i*j),
        print ""

def printMultilicationTableInWhileSquare():
    format = "%d * %d = %d, "
    i, j = 1, 1
    while(i < 10):
        j = 1
        while(j < 10):
            print format % (i, j, i * j),
            j += 1
        print ""
        i += 1

def printMultilicationTableInForTri():
    format = "%d * %d = %d, "

    for i in xrange(1, 10):
        for j in xrange(i, 10):
            print format % (i, j, i * j),
        print ""

def printMultilicationTableInWhileTri():
    format = "%d * %d = %d, "
    i, j = 1, 1
    while(i < 10):
        j = i
        while(j < 10):
            print format % (i, j, i * j),
            j += 1
        print ""
        i += 1

# ----------------------------- Calculation of the Char type variables
def calculateCharFor():
    result = ""
    for i in xrange(ord('A'), ord('Z') + 1):
        result += chr(i)
    for i in xrange(ord('a'), ord('z') + 1):
        result += chr(i)
    print result

def calculateCharWhile():
    result = ""
    i = ord('A')
    while (i < ord('Z') + 1):
        result += chr(i)
        i += 1
    i = ord('a')
    while (i < ord('z') + 1):
        result += chr(i)
        i += 1
    print result


def calculateMaxValue(a, b):
    if (a > b):
        print a
    else:
        print b


# ---------- calculate distance of two points
def distanceOf2Points(x1, y1, x2, y2):
    disX = abs(x1 - x2)
    disY = abs(y1 - y2)

    distance = (disX ** 2 + disY ** 2) ** 0.5
    print distance




# ------------------------------main function 
def main():
    printMultilicationTableInForSquare()
    print "-------------------- Task 1 ----------------------------------------"
    printMultilicationTableInWhileSquare()
    print "--------------------------------------------------------------------"
    printMultilicationTableInForTri()
    print "--------------------------------------------------------------------"
    printMultilicationTableInWhileTri()
    print "--------------------- Task 2 ---------------------------------------"
    calculateCharFor()
    print "--------------------------------------------------------------------"
    calculateCharWhile()
    print "--------------------- Task 3 ---------------------------------------"
    print "---- Calculate the maximum value of two double type variables ------"
    calculateMaxValue(1000.5, 1000)
    calculateMaxValue(500, 5000)

    try:
        calculateMaxValue('C', 'P')
        print "execute calculateMaxValue('C', 'P') successfully"
    except Error as e:
        print "Cannnot execute calculateMaxValue('C', 'P')"

    print "----- Calculate the distance of two points in 2D -------------------"
    distanceOf2Points(100, 200, -100, -400)
    distanceOf2Points(0.5, 0, 101.5, -300)
main()