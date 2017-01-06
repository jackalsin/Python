import time

def digitSum(number):
    number = abs(number)
    if (number < 10):
        return number
    else:
        return number % 10 + digitSum(number//10)

assert(digitSum(1212) == 1 + 2 + 1 + 2)
assert(digitSum(-32) == 3 + 2)
assert(digitSum(0) == 0)

print("passed digisum ")

def fib(n):
    if (n < 2):
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

assert(fib(0) == 1)
assert(fib(1) == 1)
assert(fib(2) == 2)
assert(fib(3) == 3)
assert(fib(4) == 5)
assert(fib(5) == 8)
print("fib passed")


def gcd(x, y):
    if (x < y):
        return gcd(y, x)
    elif (x % y == 0):
        return y
    else:
        return gcd(x % y, y)

assert(gcd(2**3 * 3**5 * 7**2, 2 * 3**3 * 11) == 2 * 3**3)
print("gcd passed")

def factorial(n):
    if (n == 1):
        return 1
    else:
        return n * factorial(n - 1)

assert(factorial(1) == 1)
assert(factorial(2) == 2)
assert(factorial(3) == 6)
assert(factorial(4) == 24)
assert(factorial(5) == 120)
print("factorial passed")

def isPrime(n, factor = 2):
    if (n <= 1): return False
    elif (n == 2): return True
    elif (n % 2 == 0): return False
    elif (n % factor == 0): return False
    elif (factor * factor > n):
        return True
    else:
        return isPrime(n, factor + 1)

assert(isPrime(1) == False)
assert(isPrime(2) == True)
assert(isPrime(3) == True)
assert(isPrime(4) == False)
assert(isPrime(9) == False)
assert(isPrime(13) == True)
print("isPrime passed")

def nthPrime(n, guess = 0, found = -1):
    if (n == found):
        return guess - 1
    else:
        if (isPrime(guess)):
            return nthPrime(n, guess + 1, found + 1)
        else:
            return nthPrime(n, guess + 1, found)

assert(nthPrime(0) == 2)
assert(nthPrime(1) == 3)
assert(nthPrime(2) == 5)
assert(nthPrime(3) == 7)
assert(nthPrime(4) == 11)
print("nthPrime passed")

def vowelCount(s, number = 0):
    if (len(s) == 0):
        return number
    else:
        if (s[0].lower() in "aeiou"):
            return vowelCount(s[1:], number + 1)
        else:
            return vowelCount(s[1:], number)

assert(vowelCount("I am reeeallly happy!!! :-)") == 7)
print("vowelCount passed")

def vowelCount2(s):
    if (len(s) == 0):
        return 0
    else:
        if (s[0].lower() in "aeiou"):
            return 1 + vowelCount2(s[1:])
        else:
            return vowelCount2(s[1:])

assert(vowelCount("I am reeeallly happy!!! :-)") == 7)
print("vowelCount2 passed")

# range Sum
def rangeSum(low, high):
    if (low == high):
        return low
    else:
        return low + rangeSum(low + 1, high)

assert(rangeSum(10, 15) == 75)
print("passed rangeSum")


def interleave(lsit1, list2):
    if (len(list2) == 0 or len(list2) == 0):
        return list2 + lsit1
    else:
        return ([lsit1[0]] + [list2[0]] + 
                    interleave(lsit1[1:], list2[1:]))  

assert(interleave([1,32,2],[23,4,67]) == [1,23,32,4,2,67])
print("passed the interleave")

# divide and Conquer

def rangeSum(low, high):
    if (low == high):
        return low
    else:
        mid = (low + high) //2 
        return rangeSum(low, mid) + rangeSum(mid + 1, high) 

assert(rangeSum(3, 6) == 3 + 4 + 5 + 6)

seen = dict()

def fib(n):
    if n in seen:
        return seen[n]
    if (n < 2):
        seen[1] = seen[0] = 1
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        seen[n] = result
        return result

assert(fib(1) == 1)
assert(fib(2) == 2)
assert(fib(3) == 3)
assert(fib(4) == 5)
assert(fib(5) == 8)

start1 = time.time()
print(fib(33))
end1 = time.time()
print(end1 - start1)