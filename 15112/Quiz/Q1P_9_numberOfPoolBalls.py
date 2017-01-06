def numberOfPoolBalls(rows):
    return numberOfPoolBalls(rows-1)+rows if rows else 0

def testNumberOfPoolBalls():
    print("Testing numberOfPoolBalls()...", end="")
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print("Passed.")
    print("(Add more tests to be more sure!)")

testNumberOfPoolBalls()
