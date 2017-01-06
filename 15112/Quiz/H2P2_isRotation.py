def greater(x,y):# ensure x is greater than y
    return max(x,y),min(x,y)
def digitsNumber(n):
    counter=0
    while (n!=0):
        counter+=1
        n=n//10
    return counter
def isRotation(x, y):
    x,y=greater(x,y)
    times=digitsNumber(x)
    for k in range(times):
        head=x//10**k
        tail=x%10**k
        new=tail*10**(times-k)+head
        print("k=",k,",x=",x,",y=",y,",head=",head,",tail=",tail,",new=",new)
        if (new==y):
            return True
    return False

print(isRotation(40321,321000040))