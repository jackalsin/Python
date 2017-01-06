#leastPiError
import math

def leastPiError(n):
    return abs(round(math.pi*n)/n-math.pi)

def almostEqual(d1, d2):
    epsilon = 10**-8
    return (abs(d1 - d2) < epsilon)

def testLeastPiError():
    print("Testing leastPiError()...", end="")
    assert(almostEqual(leastPiError(  7), 0.0012644893)) # at 22/7
    assert(almostEqual(leastPiError( 43), 0.0020577699)) # at 135/43
    assert(almostEqual(leastPiError(113), 0.0000002668)) # at 355/113
    print("Passed.")
    print("(Add more tests to be more sure!)")

testLeastPiError()
