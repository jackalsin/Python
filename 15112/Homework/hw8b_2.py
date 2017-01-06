# Name Zhiwei Xin
# Andrew ID: zxin
# Homework 8b

def nthLeftTruncatablePrime(n,found = -1, guess = 2):
    if isLeftTruncatablePrime(guess):
        if noZero(guess)== True:
            found+=1
    if n == found: return guess
    else:
        return nthLeftTruncatablePrime(n,found,guess+1)

def noZero(n):
    if n == 0: 
        return True
    else:
        if n%10 == 0: 
            return False
        else:
            return noZero(n//10)

def isLeftTruncatablePrime(guess):
    length = digitCounts(guess) 
    guess = abs(guess)
    if isPrime(guess) == False:
        return False
    elif length == 1: 
        return isPrime(guess) # decide if it's truncatable
    else:
        leftDigit = guess// (10**(length-1))
        return isLeftTruncatablePrime(guess - leftDigit*10**(length-1))

def isPrime(n,factor = 2):
    if n <2:
        return False
    elif n == 2:
        return True
    elif factor* factor >n:
        return True
    else:
        if n == n //factor* factor: 
            return False
        else:
            return isPrime(n,factor+1)

def testIsPrime():
    print("test of isPrime...", end = "")
    assert(isPrime(1) == False)
    assert(isPrime(2) == True)
    assert(isPrime(3) == True)
    assert(isPrime(-3) == False)
    assert(isPrime(11) == True)
    assert(isPrime(103) == True)
    assert(isPrime(131) == True)
    print("passed")

testIsPrime()


def digitCounts(guess):
    guess = abs(guess)
    if guess <10: 
        return 1
    else:
        return 1+digitCounts(guess//10)

def testDigitCounts():
    print("test of digitCounts()....", end = " ")
    assert(digitCounts(2) == 1)
    assert(digitCounts(-133) == 3)
    assert(digitCounts(0) == 1)
    print("passed")

testDigitCounts()

def testIsLeftTruncatablePrime():
    print("test of isLeftTruncatablePrime()...", end = " ")
    # assert(isLeftTruncatablePrime(2) == True)
    # assert(isLeftTruncatablePrime(3) == True)
    # assert(isLeftTruncatablePrime(10) == False)
    # assert(isLeftTruncatablePrime(947) == True)
    # assert(isLeftTruncatablePrime(12) == False)
    assert(isLeftTruncatablePrime(131) == False)    
    print("passed")

testIsLeftTruncatablePrime()


def testNthLeftTruncatablePrime():
    print("test of nthLeftTruncatablePrime()...", end = " ")
    assert(nthLeftTruncatablePrime(0) == 2)
    assert(nthLeftTruncatablePrime(1) == 3)
    assert(nthLeftTruncatablePrime(6) == 23)
    assert(nthLeftTruncatablePrime(4) == 13)
    assert(nthLeftTruncatablePrime(9) == 47)
    assert(nthLeftTruncatablePrime(15)==113)
    assert( nthLeftTruncatablePrime(16) == 137)
    print("passed")

testNthLeftTruncatablePrime()



############

def carrylessAdd(x,y):
    if x == y == 0:
        return 0
    else:
        temp =(x % 10 + y % 10)%10
        return temp + 10*carrylessAdd(x//10,y//10)

def testCarrylessAdd():
    print("test of carrylessAdd ...", end = " ")
    assert(carrylessAdd(785,376) == 51)
    assert(carrylessAdd(323,999) == 212)
    assert(carrylessAdd(348,732) == 70)
    assert(carrylessAdd(32,9) == 31)

    print("passed")

testCarrylessAdd()


#######

def longestDigitRun(n,bestDigit=9, bestCount = 1,currentCount=0,currentDigit=9):
    n = abs(n)
    if n == 0:
        if currentCount == 0:
            return 0
        else:
            return bestDigit
    else:
        if n%10 != currentDigit:
            currentCount = 1
            currentDigit = n%10
        if n%10 == n//10%10:
            currentCount += 1
        else: # end of count so compare
            if currentCount == bestCount:
                bestDigit = min(currentDigit,bestDigit)
            elif currentCount > bestCount:
                bestDigit = currentDigit
                bestCount = currentCount
        return longestDigitRun(n//10,bestDigit,bestCount,currentCount,
                                        currentDigit)

def testLongestDigitRun():
    print("test of longestDigitRun ()...", end = "")
    assert(longestDigitRun(232323) == 2)
    assert(longestDigitRun(32323333333) == 3)
    assert(longestDigitRun(32000000) == 0)
    assert(longestDigitRun(3344) ==3)
    assert(longestDigitRun(117773732) == 7)
    assert(longestDigitRun(-323) == 2)
    assert(longestDigitRun(0)==0)
    print("passed") 

testLongestDigitRun()


def longestSubpalindrome(s,startIndex = 0, endIndex = 0, bestString=''):
    if startIndex == len(s):
        return bestString
    else:
        if endIndex == len(s)+1:
            return longestSubpalindrome(s,startIndex+1,startIndex+1,bestString)
        else:
            temp = s[startIndex:endIndex]
            reverseTemp = temp[::-1]
            if temp == reverseTemp:
                if len(temp) > len(bestString):
                    bestString = temp
                elif len(temp) == len(bestString):
                    bestString = max(temp,bestString)
            return longestSubpalindrome(s,startIndex,endIndex+1,bestString)


def testLongestSubpalindrome():
    print("test of longestSubpalindrome ()...", end = "")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("32000000") == "000000")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("a") == "a")
    assert(longestSubpalindrome("") == "")
    print("passed") 

testLongestSubpalindrome()
