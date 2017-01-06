'''
This is the Assignment 1 for 12746 Assignment 1 Fall 2016
If you find this file by google in my Github, you suck!
@author Zhiwei Xin
@andrewID: zxin
'''

##!/usr/bin/python2

# print the multipllication table
def printMultilicationTableInForSquare():
    format = "%d * %d = %d, "
    for i in xrange(1, 10):
        for j in xrange(1, 10):
            print format % (i, j, i*j),
        print ""

def printMultilicationTableInWhileSquare():
    format = "%d * %d = %d, "
    i, j = 1, 1
    while(i < 10):
        j = 1
        while(j < 10):
            print format % (i, j, i * j),
            j += 1
        print ""
        i += 1

def printMultilicationTableInForTri():
    format = "%d * %d = %d, "

    for i in xrange(1, 10):
        for j in xrange(i, 10):
            print format % (i, j, i * j),
        print ""

def printMultilicationTableInWhileTri():
    format = "%d * %d = %d, "
    i, j = 1, 1
    while(i < 10):
        j = i
        while(j < 10):
            print format % (i, j, i * j),
            j += 1
        print ""
        i += 1

# ----------------------------- Calculation of the Char type variables
def calculateCharFor():
    result = ""
    for i in xrange(ord('A'), ord('Z') + 1):
        result += chr(i)
    for i in xrange(ord('a'), ord('z') + 1):
        result += chr(i)
    print result

def calculateCharWhile():
    result = ""
    i = ord('A')
    while (i < ord('Z') + 1):
        result += chr(i)
        i += 1
    i = ord('a')
    while (i < ord('z') + 1):
        result += chr(i)
        i += 1
    print result


def calculateMaxValue(a, b):
    if (a > b):
        print a
    else:
        print b


# ---------- calculate distance of two points
def distanceOf2Points(x1, y1, x2, y2):
    disX = abs(x1 - x2)
    disY = abs(y1 - y2)

    distance = (disX ** 2 + disY ** 2) ** 0.5
    print distance


def fermatTheorem(a, b, c, n):
    isSolvable = a ** n + b ** n - c ** n == 0
    if (isSolvable):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

def check_fermat():
    while True:
        inputVal = raw_input("please enter value a, b, c and n\n").strip()
        inputVal = inputVal.split()
        if len(inputVal) != 4:
            print "wrong argument number, which must be 4"
            continue
        isValidInput = True
        for elem in inputVal:
            if (not isInt(elem)):
                isValidInput = False
        if (not isValidInput):
            print "The input value must be numbers"
            continue
        a, b, c, n = int(inputVal[0]), int(inputVal[1]), int(inputVal[2]), \
                        int(inputVal[3])
        if (a < 0 or b < 0 or c < 0): 
            print "a, b, c should not be smaller than 0"
            continue
        if (n <= 2):
            print "n should be greater than 2"
            continue

        fermatTheorem(a, b, c, n)


def isInt(a):
    try:
        (int(a))
        return True
    except ValueError:
        return False

# ------------------------------ homework 4 -----------------------------------
def isPrime(x):
    if (type(x) != int): 
        return 0 
    if (x <= 1 ):
        return 0
    if (x == 2):
        return 1
    if (x % 2 == 0):
        return 0
    for i in xrange (3, int(x ** (0.5) + 1), 2):
        if (x % i == 0):
            return 0
    return 1

def largestFactor(n):
    x = 1
    while x != n:
        testNum = n / x
        if (n % x == 0):
            if isPrime(testNum):
                return testNum 
        x += 1
    return None

def allPrimeFactor(n):
    print allPrimeFactorHelper(n)

def allPrimeFactorHelper(n):
    result = [];
    if(n <= 1): return
    if (n % 2 == 0): 
        result.append(2) 
    for i in xrange(3, n + 1, 2):
        if (n % i == 0 and isPrime(i)):
            result.append(i)
    return result
        
# ------------------------------main function 
def main():
    printMultilicationTableInForSquare()
    print "-------------------- Task 1 ----------------------------------------"
    printMultilicationTableInWhileSquare()
    print "--------------------------------------------------------------------"
    printMultilicationTableInForTri()
    print "--------------------------------------------------------------------"
    printMultilicationTableInWhileTri()
    print "--------------------- Task 2 ---------------------------------------"
    calculateCharFor()
    print "--------------------------------------------------------------------"
    calculateCharWhile()
    print "--------------------- Task 3 ---------------------------------------"
    print "---- Calculate the maximum value of two double type variables ------"
    calculateMaxValue(1000.5, 1000)
    calculateMaxValue(500, 5000)

    try:
        calculateMaxValue('C', 'P')
        print "execute calculateMaxValue('C', 'P') successfully"
    except Error as e:
        print "Cannnot execute calculateMaxValue('C', 'P')"

    print "----- Calculate the distance of two points in 2D -------------------"
    distanceOf2Points(100, 200, -100, -400)
    distanceOf2Points(0.5, 0, 101.5, -300)
    
    print "--------------------- Task 4 ---------------------------------------"
    testIsPrime()
    testLargestPrime()
    testAllPrimeFactor()

def testAllPrimeFactor():
    print "test for largestPrimeFactor",
    print allPrimeFactorHelper(3)
    assert(allPrimeFactorHelper(3) == [3])
    assert(allPrimeFactorHelper(4) == [2])
    assert(allPrimeFactorHelper(5) == [5])
    assert(allPrimeFactorHelper(6) == [2, 3])
    assert(allPrimeFactorHelper(7) == [7])
    assert(allPrimeFactorHelper(8) == [2])
    assert(allPrimeFactorHelper(9) == [3])
    assert(allPrimeFactorHelper(12) == [2, 3])
    assert(allPrimeFactorHelper(2 * 11 * 17 * 23) == [2, 11, 17, 23])
    print "passed"

def testLargestPrime():
    print "test for largestPrimeFactor",
    assert(largestFactor(1) == None)
    assert(largestFactor(2) == 2)
    assert(largestFactor(3) == 3)
    assert(largestFactor(4) == 2)
    assert(largestFactor(5) == 5)
    assert(largestFactor(6) == 3)
    assert(largestFactor(7) == 7)
    assert(largestFactor(8) == 2)
    assert(largestFactor(9) == 3)
    assert(largestFactor(13) == 13)
    assert(largestFactor(15) == 5)
    assert(largestFactor(17) == 17)
    assert(largestFactor(18) == 3)
    print "passed"

# test Function
def testIsPrime():
    print "test for isPrime()",
    assert(isPrime(1) == 0)
    assert(isPrime(2) == 1)
    assert(isPrime(3) == 1)
    assert(isPrime(4) == 0)
    assert(isPrime(5) == 1)
    assert(isPrime(6) == 0)
    assert(isPrime(7) == 1)
    assert(isPrime(10) == 0)
    assert(isPrime(11) == 1)
    assert(isPrime(12) == 0)
    assert(isPrime(16) == 0)
    print "passed"
# run main function
main()

check_fermat()