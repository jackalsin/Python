def isAlmostInteger(n):
    return abs(n-round(n))<0.0001

def testIsAlmostInteger():
    print("Testing isAlmostInteger()...", end="")
    assert(isAlmostInteger(5) == True)
    assert(isAlmostInteger(5.0001) == True)
    assert(isAlmostInteger(4.9999) == True)
    assert(isAlmostInteger(5.00011) == False)
    assert(isAlmostInteger(4.99989) == False)
    assert(isAlmostInteger(-4.9999) == True)
    assert(isAlmostInteger(-5.00011) == False)
    print("Passed.")

testIsAlmostInteger()
