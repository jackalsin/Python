def brokenF(L):
    lastX = 0
    def squared(x):
        result = x**2
        lastX = x
        return result
    squaredList = [squared(x) for x in L]
    return lastX
print(brokenF(range(5)))

def fixedF(L):
    lastX = 0
    def squared(x):
        nonlocal lastX
        result = x**2
        lastX = x
        return result
    squaredList = [squared(x) for x in L]
    return lastX
print(fixedF(range(5)))
