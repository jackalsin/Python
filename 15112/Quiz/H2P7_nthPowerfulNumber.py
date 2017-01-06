import math
def almostEqual(x,y):
    if abs(x-y)<0.0000001:
        return True
def isFactor(factor,n):
    if n%factor==0:
        return True
    else:
        return False
def isSquare(n): #to test n contain a square factor
    factor=1
    limit=round(math.sqrt(n))+1
    for factor in range(1,limit):
        if isFactor(factor,n) and isFactor(factor**2,n):
            print("factor and n=", factor,", ",n)
            return True#return factor
        else:
            factor+=1
    return False

def selfSquare(n):
    divid=round(math.sqrt(n))
    if not almostEqual(divid, math.sqrt(n)):# ensure divid is integer rather round
        return False 
    #print("n and sqrt are", n,"and ",divid)
    if n%divid**2==0:
        return True
    else:
        return False

def isPowerful(n):
    guess=1
    limit=round((n)**(1/3))+1
    for factorA in range (1,limit):
        #print("we are testing factorA=",factorA,",")
        if isFactor(factorA**3,n):
            remain=n/(factorA**3)
            if selfSquare(remain):
                #print("factorA=",factorA,"remain=",remain)
                return True
    return False

def nthIsPowerfulNumber(n):
    count=0
    guess=1
    while (count<=n):
        if (isPowerful(guess)):
            count+=1
        guess+=1
    return guess-1


for i in range (11):
    print(nthIsPowerfulNumber(i))