def isFactor(f, n):
    if n==0:
        return True
    elif(f!=0):
        return n%f==0
    else:
        return False

def testIsFactor():
    print("Testing isFactor()...", end="")
    assert(isFactor(2, 2))
    assert(isFactor(2, 4))
    assert(not isFactor(2, 5))
    assert(not isFactor(0, 6))
    assert(isFactor(6, 0))
    assert(isFactor(0, 0))
    assert(isFactor(-2, 4))
    print("Passed!")

testIsFactor()
