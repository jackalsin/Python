def frequent(x,n):
    counter=0
    while (n!=0):
        if n%10==x:
            counter+=1
        n=n//10
    return counter

def mostFrequentDigit(n):
    big=0
    for i in range (10):
        if frequent(i,n)>frequent(big,n):
            big=i
    return big


print(mostFrequentDigit(11554800001115))
print(mostFrequentDigit(8787444484545))