def digitSum(n):
    n = abs(n)
    if (n == 0):
        return 0
    else:
        return (digitSum(n//10) + n%10)    



def testDigitSum():
    print("testDigitSum...", end = " ")
    assert(digitSum(1213) == 1+2+1+3)
    assert(digitSum(-133) == 1+3+3)
    print("passed")

testDigitSum()


def fib(n):
    if (n<2):
        return 1
    else:
        return fib(n-1) + fib(n-2)    

def testFib():
    print("testFib()...")
    assert([fib(n) for n in range(10)] == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
    print("passed") 

testFib()

def gcd(x,y):

    if (y==0):
        return x
    else:
        return gcd(y,x%y)

def testGcd():
    print("testGcd()...", end = '')
    assert(gcd(2**5 * 3**4 * 5**2, 2**3 * 3**8 * 7) == (2**3 * 3**4))
    print("ok!")

testGcd()

def isPrime(n,factor = 2):
    if n == 2: return True
    elif n % factor == 0:
        return False
    elif (factor * factor >= n):
        return True
    else:
        return isPrime(n,factor+1)

def testIsPrime():
    print("Test of isPrime()",end ='')
    assert(isPrime(2,) == True)
    assert(isPrime(3,2)== True)
    assert(isPrime(5,2)== True)
    assert(isPrime(15,2)== False)
    print("passed")

testIsPrime()

def nthPrime(n,found = -1,guess = 2):
    if isPrime(guess, ): found+=1
    if found == n: return guess
    else:
        return nthPrime(n,found,guess+1)

print([nthPrime(i) for i in range(10)])
assert([nthPrime(i) for i in range(10)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
print("ok!")



def vowelCount(s):
    if s == '':
        return 0
    else:
        if s[0].upper() in 'AEOIU':
            return (1 + vowelCount(s[1:]))
        else: return (vowelCount(s[1:]))
print("test of vowelCount", end = ' ')
assert(vowelCount("I am reeeallly happy!!! :-)") == 7)
print("ok!")


############ Practice 
def sumOfOdd(L):
    if len(L) == 0:
        return 0
    else:
        if L[0]%2 == 1:
            return L[0] + sumOfOdd(L[1:])
        else:
            return sumOfOdd(L[1:])









def testSumOfOdd():
    print("test of sumOfodd",end = " ")
    assert(sumOfOdd([1,3,5,7,10,23]) == 39)
    print("passed")

testSumOfOdd()


def hasConsecutiveDigits(n):
    n = abs(n)
    if n < 10:
        return False
    else:
        ones = n%10
        tens = n//10%10
        if (ones == tens):
            return True
        else:
            return hasConsecutiveDigits(n//10)

def testHasConsecutiveDigit():
    print("test of hasConsecutiveDigits()...",end = '')
    assert(hasConsecutiveDigits(1213133) == True)
    assert(hasConsecutiveDigits(323235623) == False)
    assert(hasConsecutiveDigits(0) == False)

    print("passed")

testHasConsecutiveDigit()


def minList(L):
    if len(L) == 1:
        return L[0]
    else:
        if L[0] < minList(L[1:]):
            return L[0]
        else:
            return minList(L[1:])
def testMinList():
    print("test of minList()",end = "")
    assert(minList([3,25,342,0,2,11,3]) == 0)
    assert(minList([13,-23,32,33,333,-33]) == -33)
    print("passed")

testMinList()


def isPerfectNumber(n,factor = 1,sum = 0):
    if factor * 2 > n:
        return sum == n
    else:
        if (n ==( n// factor * factor)):
            sum += factor
        return isPerfectNumber(n,factor+1,sum)


print(isPerfectNumber(28))

def testIsPerfectNumber():
    print("test of isPerfectNumber",end = "")
    assert(isPerfectNumber(6) == True)
    assert(isPerfectNumber(28) == True)
    assert(isPerfectNumber(7) == False)
    print("passed")


testIsPerfectNumber()