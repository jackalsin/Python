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



# ------------------------------main function 
def main():
    printMultilicationTableInForSquare()
    print "--------------------------------------------------------------------"
    printMultilicationTableInWhileSquare()
    print "--------------------------------------------------------------------"
    printMultilicationTableInForTri()
    print "--------------------------------------------------------------------"
    printMultilicationTableInWhileTri()
    print "--------------------------------------------------------------------"


main()