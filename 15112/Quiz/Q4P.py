# areaOfPolygon(L) 

def areaOfPolygon(L):
    area=0
    for i in range(len(L)):
        (x0,y0)=L[i]
        (x1,y1)=L[(i+1)%len(L)]
        area+=0.5*(x0*y1-x1*y0)

    return abs(area) # place your answer here!
 
def almostEqual(d1, d2):
    epsilon = 10**-8
    return abs(d1 - d2) < epsilon

def testAreaOfPolygon():
    print("Testing areaOfPolygon()...", end="")
    assert(almostEqual(areaOfPolygon([(4,10), (9,7), (11,2), (2,2)]), 45.5))
    assert(almostEqual(areaOfPolygon([(9,7), (11,2), (2,2), (4, 10)]), 45.5))
    assert(almostEqual(areaOfPolygon([(0, 0), (0.5,1), (1,0)]), 0.5))
    assert(almostEqual(areaOfPolygon([(0, 10), (0.5,11), (1,10)]), 0.5))
    assert(almostEqual(areaOfPolygon([(-0.5, 10), (0,-11), (0.5,10)]), 10.5))
    print("Passed!")

testAreaOfPolygon()

# question 3 evalPolynomial(coeffs, x) 


def evalPolynomial(coeffs, x):
    sum=0
    coeffs.reverse()
    for i in range (len(coeffs)):    
        sum+=coeffs[i]*x**i
    return sum # place your answer here!

def testEvalPolynomial():
    print("Testing evalPolynomial()...", end="")
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    assert(evalPolynomial([2,3,0,4], 4) == 180)
    # f(x) = 6, f(42) = 6
    assert(evalPolynomial([6], 42) == 6)
    # f(x) = 6x^2 -2x - 20, f(-1) = -12
    assert(evalPolynomial([6,-2,-20], -1) == -12)
    # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
    assert(evalPolynomial([6,0,-8,0,-8,0], 2) == 112)
    assert(evalPolynomial([6,0,-8,0,-8,0], 1) == -10)
    assert(evalPolynomial([6,0,-8,0,-8,0], 0) == 0)
    print("Passed!")

testEvalPolynomial()


#Question 4 
def multiplyPolynomials(p1, p2):
    p3=[0]*(len(p1)+len(p2)-1)
    p1.reverse()
    p2.reverse()
    for i in range (len(p1)):
        for j in range (len(p2)):
            p3[i+j]+=p1[i]*p2[j]
            # print(p3[i+j],p1[i],p2[j])
    p3.reverse()
    # this p3.reveerse() returns None, and can't be printed.
    return p3 # place your answer here!

def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    # (2)*(3) == 6
    assert(multiplyPolynomials([2], [3]) == [6])
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert(multiplyPolynomials([2,-4],[3,5]) == [6,-2,-20])
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert(multiplyPolynomials([2,0,-4],[3,0,2,0]) == [6,0,-8,0,-8,0])
    print("Passed!")

testMultiplyPolynomials()


# Question 5 Repeating Pattern
def repeatingPattern(L):
    if len(L)==0: return None
    for i in range (1,len(L)//2+1):
        pattern=L[:i]
        repeatNum=len(L)//(i)
        # print("pattern and repeat Num",len(L), i+1,pattern, repeatNum)
        if pattern*repeatNum == L:
            # print(L,repeatNum)
            return (pattern,repeatNum)
    return None

def testRepeatingPattern():
    print("Testing repeatingPattern()...", end="")
    assert(repeatingPattern([]) == None)
    assert(repeatingPattern([42]) == None)
    assert(repeatingPattern([1,2]) == None)
    assert(repeatingPattern([1,1]) == ([1], 2))
    assert(repeatingPattern([1,2,1]) == None)
    assert(repeatingPattern([1,2,3,1,2,3]) == ([1,2,3], 2))
    assert(repeatingPattern([1,2,3,1,2]) == None)
    assert(repeatingPattern([1,2,3,1,2,3,1]) == None)
    L = list(range(10))
    assert(repeatingPattern(L*20) == (L, 20))
    print("Passed!")

testRepeatingPattern()


def isNearlySorted(L):
    if L== sorted(L):
        return False
    for i in range(len(L)):
        for j in range(i,len(L)):
            L[i],L[j]=L[j],L[i]
            if L==sorted(L):
                return True
            L[i],L[j]=L[j],L[i]
    return False # place your answer here!

def testIsNearlySorted():
    print("Testing isNearlySorted()...", end="")
    assert(isNearlySorted([0,1,2,3]) == False)
    assert(isNearlySorted([]) == False)
    assert(isNearlySorted([42]) == False)
    assert(isNearlySorted([3,2]) == True)
    assert(isNearlySorted([2,2]) == False)
    assert(isNearlySorted([5,2,3,4,1,6]) == True)
    assert(isNearlySorted([1,2,3,5,4]) == True)
    print("Passed!")

testIsNearlySorted()
