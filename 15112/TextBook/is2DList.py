# to check a 2d list
def isReg(a):
    if len(a)==0:
        return False
    if len(a[0])==0:
        return True
    rows=len(a)
    col0=len(a[0])
    for row in range (1,rows):
        if col0 != len(a[row]):
            return False
    return True

def testIsReg():
    print("Test of isReg()...", end = ' ')
    assert(isReg([])==False)
    assert(isReg([[1,2,3],[2,3,4]])==True)
    assert(isReg([[1,3,3],[2,34]])==False)
    assert(isReg([[1,3,3],[]])==False)

    assert(isReg([[]])==True)
    print("passed")

testIsReg()

def seivePrime(a):
    primeList=[[True]*(a+1)]
    primeList[0]=primeList[1]=False
    for item in range(primeList):
        for mul in (item*2, primeList,prime):
            primeList[mul]=False

