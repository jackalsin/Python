def digitCount(n):
    if n==0:
        return 1
    n=abs(n)
    count=0
    while (n!=0):
        count+=1
        n=n//10
    return count # replace with your solution

def testDigitCount():
    print("Testing digitCount()...", end="")
    assert(digitCount(3) == 1)
    assert(digitCount(33) == 2)
    assert(digitCount(3030) == 4)
    assert(digitCount(-3030) == 4)
    assert(digitCount(0) == 1)
    print("Passed!")

testDigitCount()
