def mergesort(L):
    if (len(L) < 2):
        return L
    else:
        mid = len(L)//2
        left = mergesort(L[:mid])
        right = mergesort(L[mid:])
        return merge(left, right)
def merge(L1,L2):
    if (len(L1) == 0):
        return L2
    if (len(L2) == 0):
        return L1

    if(L1[0] < L2[0]):
        return [L1[0] ]+ [L2[0]] + merge(L1[1:],L2[1:])
    else:
        return [L2[0]] + [L1[0] ]+ merge(L1[1:],L2[1:])

print(mergesort([2,34,5,6.2,3,4,6]))