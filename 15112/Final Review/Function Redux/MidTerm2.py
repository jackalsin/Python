def ct1(L):
    if (len(L) < 2):
        return []
    else:
        f = lambda *args: len(args) + sum(args)
        mid = len(L)//2
        return ct1(L[:mid]) + [f(*L)] +ct1(L[mid:])

print(ct1([1,2,0,4,3]))

def rc1(L):
    assert(L == list(reversed(sorted(L))))
    assert(L != list(reversed(sorted(set(L)))))
    assert(len(L) % 2 == 0)
    assert(max(L) < 10)
    def f(L):
        if (L == []):
            return []
        else:
            return [L[0] * L[1]] + f(L[1:-1])
    return (f(L) == [10,20])

rc1([5,5,4,2])
print("we passsss")

print()



def testWithCallCounter():
    print("Testing @withCallCounter...")
    @withCallCounter
    def f(x,y): return x*y
    assert(getCallCounter(f) == 0)
    assert(f(2,3) == 6)
    assert(getCallCounter(f) == 1)
    assert(f(3,2) == 6)
    assert(getCallCounter(f) == 2)
    print()
    @withCallCounter
    def h(a,b,c,d,e): return a+b+c+d+e
    assert(getCallCounter(h) == 0)
    assert(h(1,2,3,4,5) == 1 +2+3+4+5)
    assert(getCallCounter(h) == 1)
    print("passed")

d = dict()

def withCallCounter(a):
    def g(*args):
        print("g = ", g.__name__,"a = ", a.__name__, "a = ",a)
        if a not in d:
            d[a.__name__] = 1
        else:
            d[a.__name__] = d[a.__name__] + 1
        print("     after d = ",d)
        return a(*args)

    print("before d = ", d)
    return g

def getCallCounter(g):
    if g in d:
        return d[g]
    else:
        return 0





testWithCallCounter()