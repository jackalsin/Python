def insertionsort(L):
    if (len(L) < 2):
        return L
    else:
        first = L[0]
        rest = insertionsort(L[1:])
        lo = [x for x in rest if x < first]
        hi = [x for x in rest if x >= first]
        return lo + [first] + hi

print(insertionsort([1,5,3,4,2,0]))
