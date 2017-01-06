import math
def isPrime(n):
    if n<2: return False
    elif (n==2):return True
    else:
        limit=round(math.sqrt(n))+1
        for i in range(2,limit,1):
            if n%i==0:
                return False
    return True

def digitsNum(n):
    n=abs(n)
    if n==0: return 1
    count=0
    while (n):
        count+=1
        n=n//10
    return count
def ifPalindromic(n):
    digits=digitsNum(n)
    for k in range(1,digits//2+1): #this can be more accurate
        tail=n%10
        head=n//10**(digitsNum(n)-1)
        #print("tail=", tail, ", head=", head)
        if head!=tail:
            return False
        n=(n-tail-head*10**(digitsNum(n)-1))//10
#        print ("n=",n)
    return True

def nthPalindromicPrime(n):
    i=0
    guess=0
    while (i<=n):
        if ifPalindromic(guess) and isPrime(guess):
            i+=1
            #print(guess)
        guess+=1
    return guess-1
