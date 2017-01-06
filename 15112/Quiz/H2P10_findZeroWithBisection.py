#findZerosWithBisection 
def almostEqual(x,y):
    return abs(x-y)<1e-8

def switch (a,b):
    if a>b:
        c=a
        a=b
        b=c
        return a,b
    else:
        return a,b

def equalsToValue(f,a,b,c):
    if f(a)*f(c)<0: 
        return a,c
    else:
        return c,b

def findZeroWithBisection(f,a,b,epsilon):
    midPoint=(a+b)/2
    #make sure the function to positive or not
    while abs(f(midPoint))>epsilon:
        if f(midPoint)==0:
            return midPoint
        elif f(midPoint)>0:
            print("Since greater than 0. Now we are checking a=", a, "and b=",b)
            a,b=equalsToValue(f,a,b,midPoint)
        else:
            print("Since smaller than 0. Now we are checking a=", a, "and b=",b)
            a,b=equalsToValue(f,a,b,midPoint)
        midPoint=(a+b)/2
    return midPoint

print ("use bisection to approximate x where x**5 == 2**x")
def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
x = findZeroWithBisection(f3, 1, 2, 0.000000001)
print (" x =", x                              )# prints x = 1.17727855081
print (" check: x**5 - 2**x =", (x**5 - 2**x)) # prints check: x**5 - 2**x = 3.63570817896e-09 (great!)

