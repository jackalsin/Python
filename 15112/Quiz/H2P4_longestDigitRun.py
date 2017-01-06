def run(i,n): # return how many run i has in num
    if n==0: return 1
    count=0
    while (n):
        previous=n%10
        if previous==i:
            count+=1
        n=n//10
    return count

def longestDigitRun(n):
    n=abs(n)
    longestRunDigits=0
    for i in range(10):
        iRun=run(i,n)
        if iRun>longestRunDigits:
            longestRunDigits=i       
    return longestRunDigits

print(longestDigitRun(-677886))

print(longestDigitRun(117773732))