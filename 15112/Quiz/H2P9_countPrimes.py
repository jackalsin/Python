#countingPrimes 
import math
def isPrime(n):
    if n<2: 
        return 0
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        limit =round(math.sqrt(n))+1
        for i in range(3,limit,2):
            if n%i==0:
                return False
        return True
# print(isPrime(13))
def pi(n):
    count=0
    for i in range(n+1):
        if isPrime(i):
            count+=1
    return count
def testCountingPrimes():
    assert(pi(1) == 0)
    assert(pi(2) == 1)
    assert(pi(3) == 2)
    assert(pi(4) == 2)
    assert(pi(5) == 3)
    assert(pi(100) == 25)  # there are 25 primes in the range [2,100]
    print ("Passed all tests!")

testCountingPrimes()