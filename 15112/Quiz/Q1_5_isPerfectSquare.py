def almostEqual(a,b):
    return abs(a-b)<0.00000001
def isPerfectSquare(n):
    if n>=0:
        return almostEqual(n**0.5,round(n**0.5))
    else:
        return False

def testIsPerfectSquare():
    print("Testing isPerfectSquare...", end="")
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(32) == False)
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(-16) == False)
    print("Passed!")

testIsPerfectSquare()
