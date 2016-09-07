def maxSubArraySum(a):

    maxSoFar =a[0]
    maxEndHere = a[0]

    for i in range(1,a.__len__()):
        maxEndHere = max(a[i], maxEndHere + a[i])
        maxSoFar = max(maxSoFar,maxEndHere)

    return maxSoFar



aList = [1,3,-2,-3,0,6,7]

print(maxSubArraySum(aList) )
