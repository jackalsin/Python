def variableArgs(*args):
    print("*args = ",*args)
    print("args =", args)

variableArgs("thank", "olve", "wwe")


# lambda Functions
myF = lambda x: 4*x +2

print("myF(4)", myF(4))


# function inside function
def f(L):
    def squared(x): return x**2
    print(type(L))
    return [squared(x) for x in L]
print(f(range(5)))

try:
    print(squared(5))
except:
    print("squared is not defined outside f")


# function decorator
def derivativeFn(f):
    def g(x):
        h = 10**-5
        return (f(x+h) - f(x))/h
    return g
    
@derivativeFn
def h(x): return 5*x**3 + 10
print(h(3)) # 135, matches fprime1 from above.

