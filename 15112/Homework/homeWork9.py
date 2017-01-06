# good day to hunt


def isPrime(n):
    if n<2:
        return False
    if n == 2:
        return True
    if(n%2 == 0):return False
    
    for i in range(3,int(n**0.5+1),2):
        if n%i == 0:
            return False
    return True

print(isPrime(202))

def findRTP(digits,number = 0):
    if digits == 0:
        return number
    else:
        for appendNum in range(10):
            number = number * 10 + appendNum
            if isPrime(number):
                solution = findRTP(digits-1, number)
                if solution:
                    return solution
            number//=10

print(findRTP(3))