#circlesIntersect
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def circlesIntersect(x1, y1, r1, x2, y2, r2):
    return distance(x1,y1,x2,y2)<=(r1+r2)

def testCirclesIntersect():
    print("Testing circlesIntersect()...", end="")
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testCirclesIntersect()
