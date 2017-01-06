class A(object):
    """docstring for A"""
    def __init__(self, arg):
        self.arg = arg

    def __eq__(self, other):
        return (isinstance(other, A) and self.arg == other.arg) 

    def __hash__(self):
        return hash(self.arg)

s = set()
s.add(A(5))
print(A(5) in s)

import random
def splitLineToMakeTriangle():
    trials = 10000
    success = 0
    size = 1
    for i in range(trials):
        if canTri(size):
            success += 1

    return success/trials

def canTri(size):
    a = random.randrange(0,size*10000)/10000
    b = random.randrange(0,size*10000)/10000
    (a,b)  = (min(a,b), max(a,b))
    l1 = a
    l2 = b - a
    l3 = size - b
    result = ((l1 + l2) > l3 and (l2 + l3) > l1 and (l1 + l3) > l2)
    return result


print(splitLineToMakeTriangle())