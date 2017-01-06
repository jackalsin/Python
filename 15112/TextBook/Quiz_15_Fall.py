x=2 
def f(x):
    x+=2
    return x
def g(y):
    global x
    x*=2
    return x+y
def ct2(n):
    result=""
    for i in range(n):
        result+=str(g(f(i)))+'.'
    return result

print(ct2(3))