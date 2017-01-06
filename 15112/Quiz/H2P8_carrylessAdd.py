import math
def kthDigit(n,k):
    return (n//10**k)%10
def digitCounts(n):
    n=abs(n)
    if n==0: return 1
    count=0
    while n:
        count+=1
        n//=10
    return count
print(digitCounts(1))
#
def carrylessAdd(x,y):
    sum=0
    digits=digitCounts(max(x,y))
    for i in range (digits):
        xKthDigit=kthDigit(x,i)
        yKthDigit=kthDigit(y,i)
        digitSum=(xKthDigit+yKthDigit)%10
        sum+=digitSum*10**i
    return sum


print(carrylessAdd(785,376))
print(carrylessAdd(0,0))