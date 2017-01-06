#Test Function
def onesDigit(x):
    return x%10

def testOnesDigit():
    print("Testing onesDigit()...",end=" ")
    assert(onesDigit(5))==5
    assert(onesDigit(123))==3
    assert(onesDigit(100))==0
    assert(onesDigit(999))==9
    assert(onesDigit(-123))==3
    print("Passed")

testOnesDigit()
