# hw1.py
# Zhiwei Xin + zxin + AA

import math

def almostEqual(d1, d2):
    epsilon = 10**-8
    return (abs(d2 - d1) < epsilon)

def nearestBusStop(street):
    return (street+3)//8*8

def setKthDigit(n, k, d):
    digits=n//10**k-n//10**(k+1)*10
    rest=n-digits*10**k
    return rest+d*10**k

def cosineZerosCount(r):
    return int((r-math.pi/2)/(math.pi))+1 if r>=math.pi/2 else 0

def riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent):
    T=totalTime
    D=totalDistance/2
    C=riverCurrent
    V=(2*D+math.sqrt(4*D*D+4*T*T*C*C))/(2*T)
    denominator=2*D/T
    return ((C+V)/2/V*T)

##################
def pointInRec(x1, y1, left2, top2, width2, height2):
    return ((x1>=left2 and y1>=top2) and (x1<=(left2+width2)) and
     (y1<=(top2+height2)))

def rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2):
    return (pointInRec(left1, top1, left2, top2, width2, height2) or 
        pointInRec(left1+width1, top1, left2, top2, width2, height2) or 
        pointInRec(left1, top1+height1, left2, top2, width2, height2) or 
        pointInRec(left1+width1, top1+height1, left2, top2, width2, height2))
#####################  
def lineIntersection(m1, b1, m2, b2):
    return (b2-b1)/(m1-m2) if m1!=m2 else None

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def triangleArea(s1, s2, s3):
    s=(s1+s2+s3)/2
    return math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1=lineIntersection(m1,b1,m2,b2)
    x2=lineIntersection(m3,b3,m2,b2)
    x3=lineIntersection(m3,b3,m1,b1)
    if x1==None and x2==None and x3==None:
        return 0
    else:
        y1=m1*x1+b1
        y2=m2*x2+b2
        y3=m3*x3+b3
    aSide=distance(x1,y1,x2,y2)
    bSide=distance(x2,y2,x3,y3)
    cSide=distance(x3,y3,x1,y1)
    return triangleArea(aSide,bSide,cSide)


############## Solution for Bonus
def oneThirdthPower(x):
    return x**(1/3) if x>=0 else -(-x)**(1/3)

def realRoot(a,b,c,d):
    p=-b/3/a
    q=p**3+(b*c-3*a*d)/(6*a*a)
    r=c/3/a
    delta=q**2+(r-p**2)**3
#    print (p, '\n', q, '\n',r,'\n',delta)# test only
    if delta>=0:
        x=oneThirdthPower(q+math.sqrt(delta))+oneThirdthPower(q-math.sqrt(delta))+p
#        print('delta is greater than or equals to zero, and x=', x)
        #for test lonly
        return x
    else:
        x=(((q+math.sqrt(-delta)*1j)**(1/3))+((q-math.sqrt(-delta)*1j))**(1/3)+p)
#        print ('delta is smaller than zero, and x=', round(x.real)) #test only
        return round(x.real)
def otherRoots(r,a,b,c,d):
    delta=b*b-4*a*c-2*a*b*r-3*a*a*r*r
    if delta<=0.00000000001:
        delta = 0
    return (-b-r*a-math.sqrt(delta))/2/a, (-b-r*a+math.sqrt(delta))/2/a

def increase(a,b,c):
    return min(a,b,c), a+b+c-max(a,b,c)-min(a,b,c), max(a,b,c)

def findIntRootsOfCubic(a,b,c,d):
    root1=realRoot(a,b,c,d)
    root2,root3=otherRoots(root1,a,b,c,d)
    a,b,c=increase(root1,root2,root3)
    return a,b,c


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def testNearestBusStop():
    print("Testing nearestBusStop()...", end="")
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(4) == 0)
    assert(nearestBusStop(5) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    assert(nearestBusStop(20) == 16)
    assert(nearestBusStop(21) == 24)
    print("Passed. (Add more tests to be more sure!)")

def testSetKthDigit():
    print("Testing setKthDigit()...", end="")
    assert(setKthDigit(468, 0, 1) == 461)
    assert(setKthDigit(468, 1, 1) == 418)
    assert(setKthDigit(468, 2, 1) == 168)
    assert(setKthDigit(468, 3, 1) == 1468)
    print("Passed. (Add more tests to be more sure!)")

def testCosineZerosCount():
    print("Testing cosineZerosCount()...", end="")
    assert(type(cosineZerosCount(0)) == int)
    assert(cosineZerosCount(0) == 0)
    assert(cosineZerosCount(math.pi/2 - 0.0001) == 0)
    assert(cosineZerosCount(math.pi/2 + 0.0001) == 1)
    assert(cosineZerosCount(3*math.pi/2 - 0.0001) == 1)
    assert(cosineZerosCount(3*math.pi/2 + 0.0001) == 2)
    assert(cosineZerosCount(5*math.pi/2 - 0.0001) == 2)
    assert(cosineZerosCount(5*math.pi/2 + 0.0001) == 3)
    assert(cosineZerosCount(-math.pi/2 - 0.0001) == 0)
    assert(cosineZerosCount(-math.pi/2 + 0.0001) == 0)
    print("Passed. (Add more tests to be more sure!)")

def testRiverCruiseUpstreamTime():
    print("Testing riverCruiseUpstreamTime()...", end="")
    # example from the source notes:
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 2 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime,
                                               totalDistance,
                                               riverCurrent),
                       1.7888736053508778)) # 1.79 in notes
    # another simple example
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 0 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime,
                                               totalDistance,
                                               riverCurrent),
                       1.5))
    print("Passed. (Add more tests to be more sure!)")

def testRectanglesOverlap():
    print("Testing rectanglesOverlap()...", end="")
    assert(type(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2)) == bool)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    print("Passed. (Add more tests to be more sure!)")

def testLineIntersection():
    print("Testing lineIntersection()...", end="")
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(almostEqual(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(almostEqual(lineIntersection(10,0,-4,35), 2.5))
    print("Passed. (Add more tests to be more sure!)")

def testDistance():
    print("Testing distance()...", end="")
    assert(almostEqual(distance(0, 0, 1, 1), 2**0.5))
    assert(almostEqual(distance(3, 3, -3, -3), 6*2**0.5))
    assert(almostEqual(distance(20, 20, 23, 24), 5))
    print("Passed. (Add more tests to be more sure!)")

def testTriangleArea():
    print("Testing triangleArea()...", end="")
    assert(almostEqual(triangleArea(3,4,5), 6))
    assert(almostEqual(triangleArea(2**0.5, 1, 1), 0.5))
    assert(almostEqual(triangleArea(2**0.5, 2**0.5, 2), 1))
    print("Passed. (Add more tests to be more sure!)")

def testThreeLinesArea():
    print("Testing threeLinesArea()...", end="")
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    print("Passed. (Add more tests to be more sure!)")

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    observed = findIntRootsOfCubic(a,b,c,d)
    actual = tuple(sorted([z1,z2,z3]))
    assert(observed == actual)

def testBonusFindIntRootsOfCubic():
    # only test the bonus if they tried it...
    if ("findIntRootsOfCubic" not in globals()): return
    print("Testing findIntRootsOfCubic()...", end="")
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    testFindIntRootsOfCubicCase(1,1,-5,3)
    print("Passed. (Add more tests to be more sure!)")
 
def testAll():
    testNearestBusStop()
    testSetKthDigit()
    testCosineZerosCount()
    testRiverCruiseUpstreamTime()
    testRectanglesOverlap()
    testLineIntersection()
    testDistance()
    testTriangleArea()
    testThreeLinesArea()
    testBonusFindIntRootsOfCubic()
 
if __name__ == "__main__":
    testAll()