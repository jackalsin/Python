import math

def almostEqual(d1, d2):
    epsilon = 10**-8
    return (abs(d1 - d2) < epsilon)

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    a=distance(x1,y1,x2,y2)
    b=distance(x1,y1,x3,y3)
    c=distance(x2,y2,x3,y3)
    return (almostEqual(a**2+b**2,c**2) or almostEqual(c**2+b**2,a**2) or almostEqual(a**2+c**2,b**2)) # replace with your solution

def testIsRightTriangle():
    print("Testing isRightTriangle()...", end="")
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testIsRightTriangle()
