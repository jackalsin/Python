def hasConsecutiveDigits(n):
#    print("We are testing n=",n)
    if n==0: 
        return False
    else:
        n=abs(n)
        while (n!=0):
            previous=(n//10)%10
 #           print (previous)
            current=n%10
#            print(current)
            if (current==previous):
                return True
            n=n//10
    return False # replace with your solution

def testHasConsecutiveDigits():
    print("Testing hasConsecutiveDigits()...", end="")
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print("Passed!")

testHasConsecutiveDigits()
