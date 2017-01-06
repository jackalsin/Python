import math
def cosineError(x, k):
    sum=0
    if k==0: 
        return abs(math.cos(x)-1)
    for i in range (k+1):
        add=(-1)**i*x**(2*i)/(math.factorial(2*i))
        sum+=add
    return abs(math.cos(x)-sum) # replace with your solution

def almostEqual(d1, d2):
    epsilon = 10**-8
    return abs(d1 - d2) < epsilon

def testCosineError():
    print("Testing cosineError()...", end="")
    assert(almostEqual(cosineError(0, 0), abs(math.cos(0) - 1)))
    assert(almostEqual(cosineError(1, 0), abs(math.cos(1) - 1)))
    x = 1.2
    guess = 1 - x**2/2 + x**4/(4*3*2)
    error = abs(math.cos(x) - guess)
    assert(almostEqual(cosineError(x, 2), error))
    x = 0.75
    guess = 1 - x**2/2 + x**4/(4*3*2) - x**6/(6*5*4*3*2)
    error = abs(math.cos(x) - guess)
    assert(almostEqual(cosineError(x, 3), error))
    print("Passed!")

testCosineError()
