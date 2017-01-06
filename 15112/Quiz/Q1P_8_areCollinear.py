import math
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def almostequal(x,y):
    return abs(x-y)<0.000001
def areCollinear(x1, y1, x2, y2, x3, y3):
    a=distance(x1,y1,x2,y2)
    b=distance(x1,y1,x3,y3)
    c=distance(x2,y2,x3,y3)
    return almostequal(a+b,c) or almostequal(a+c,b) or almostequal(b+c,a)

def testAreCollinear():
    print("Testing testAreCollinear()...", end="")
    assert(areCollinear(0, 0, 1, 1, 2, 2) == True)
    assert(areCollinear(0, 0, 1, 1, 2, 3) == False)
    assert(areCollinear(1, 1, 0, 0, 2, 2) == True)
    assert(areCollinear(1, 1, 0, -1, 2, 2) == False)
    assert(areCollinear(2, 0, 2, 1, 2, 2) == True)
    assert(areCollinear(2, 0, 2, 1, 3, 2) == False)
    assert(areCollinear(3, 0, 2, 1, 3, 2) == False)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testAreCollinear()
