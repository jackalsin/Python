import math
def numberOfPoolBallRows(balls):
    return math.ceil((-1+math.sqrt(1+8*balls))/2)

def testNumberOfPoolBallRows():
    print("Testing numberOfPoolBallRows()...", end="")
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testNumberOfPoolBallRows()
