def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def triangleArea(x1, y1, x2, y2, x3, y3):
    a=distance(x1, y1, x2, y2)
    b=distance(x1, y1, x3, y3)
    c=distance(x3, y3, x2, y2)
    s=0.5*(a+b+c)
    return (s*(s-a)*(s-b)*(s-c))**0.5

    
def almostEqual(d1, d2):
    epsilon = 0.00001
    return abs(d1-d2) <= epsilon

def testTriangleArea():
    print("Testing triangleArea...", end="")
    assert(almostEqual(triangleArea(0, 0, 0, 2, 2, 0), 2.0))
    assert(almostEqual(triangleArea(0, 0, 4, 0, 2, 6), 12.0))
    assert(almostEqual(triangleArea(0, 0, -4, 0, -2, -6), 12.0))
    print("Passed!")

testTriangleArea()
