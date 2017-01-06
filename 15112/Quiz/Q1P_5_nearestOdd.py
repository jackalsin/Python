def nearestOdd(n):
    return (n//2*2+1) if n%2!=0 else (n-1)
def testNearestOdd():
    print("Testing nearestOdd()...", end="")
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testNearestOdd()
