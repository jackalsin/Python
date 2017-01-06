#nthFibonacci(n)
def nthFibonacci(n):
    n=n+1
    left=(1+5**0.5)**n
    right=(1-5**0.5)**n
    bottom=(2**n)*(5**0.5)
    return round((left-right)/(bottom))
def testNthFibonacci():
    print("Testing nthFibonacci()...", end="")
    assert(nthFibonacci(0) == 1)
    assert(nthFibonacci(1) == 1)
    assert(nthFibonacci(2) == 2)
    assert(nthFibonacci(3) == 3)
    assert(nthFibonacci(4) == 5)
    assert(nthFibonacci(5) == 8)
    assert(nthFibonacci(6) == 13)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testNthFibonacci()
