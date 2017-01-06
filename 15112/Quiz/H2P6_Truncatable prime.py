import math
def isPrime(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        limit=round(math.sqrt(n))+1
        for i in range (3,limit,2):
            if n%i==0:
                return False
    return True
def digitsNum(n):
    n=abs(n)
    if n==0:
        return 1
    count=0
    while n:
        count+=1
        n=n//10
    return count
def leftTrunc(n):
    ###leftTruc
    digitsNumber=digitsNum(n)
    #print ("we are going to truc ",n ,end=" ")
    Head=n//10**(digitsNum(n)-1)
    #print("Head=",Head)
    n=n-Head*10**(digitsNum(n)-1)
    #print("after truc is ", n)
    return n


def LeftTruncatablePrime(n):
    while n:
        if not isPrime(n):
            #print("Now we are entering True")
            return False
        else:
            #print("Now we are entering LeftTrunc")
            n=leftTrunc(n)
            #print("after truc n=",n)
    return True


def nthLeftTruncatablePrime(n):
    count=0
    guess=2
    while(count<=n):
        if LeftTruncatablePrime(guess):
            count+=1
            #print(guess)
        guess+=1
    return guess-1
#print(LeftTruncatablePrime(19))
print(nthLeftTruncatablePrime(10))