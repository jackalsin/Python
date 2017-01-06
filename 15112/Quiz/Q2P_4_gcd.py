def greater(x,y):
    if (x<y): #make sure x is greater than y
        b=y
        y=x
        x=b
    return x,y
def gcd(x, y):
    x,y=greater(x,y)
#    print("Now we are teseting", x,' ', y )
    while (x%y!=0):
        x,y=greater(x,y)
 #       print ('before x=',x, 'y=',y)
        temp=x
        x=y
        y=temp%y
#        print ('x=',x, 'y=',y)
        if y==0:
#            print ("now we are returing 1") 
            return 1
#    print("Now we are returning ", y)
    return y

def testGcd():
    print("Testing gcd()...", end="")
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    x = 1568160 # 2**5 * 3**4 * 5**1 *        11**2
    y = 3143448 # 2**3 * 3**6 *        7**2 * 11**1
    g =    7128 # 2**3 * 3**4 *               11**1
    assert(gcd(x, y) == g)
    print("Passed!")

print()

testGcd()
