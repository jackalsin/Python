# recursive-sorts.py

import time, random, copy

def selectionsort(L):
    if (len(L) < 2):
        return L
    else:
        i = L.index(min(L))
        return [L[i]] + selectionsort(L[:i] + L[i+1:])

def insertionsort(L):
    if (len(L) < 2):
        return L
    else:
        first = L[0]
        rest = insertionsort(L[1:])
        lo = [x for x in rest if x < first]
        hi = [x for x in rest if x >= first]
        return lo + [first] + hi

def quicksort(L):
    if (len(L) < 2):
        return L
    else:
        first = L[0]  # pivot
        rest = L[1:]
        lo = [x for x in rest if x < first]
        hi = [x for x in rest if x >= first]
        return quicksort(lo) + [first] + quicksort(hi)

def merge(A, B):
    # beautiful, but impractical for large N
    if ((len(A) == 0) or (len(B) == 0)):
        return A+B
    else:
        if (A[0] < B[0]):
            return [A[0]] + merge(A[1:], B)
        else:
            return [B[0]] + merge(A, B[1:])

def merge(A, B):
    # iterative (ugh) and destructive (double ugh), but practical...
    C = [ ]
    i = j = 0
    while ((i < len(A)) or (j < len(B))):
        if ((j == len(B)) or ((i < len(A)) and (A[i] <= B[j]))):
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    return C

def mergesort(L):        
    if (len(L) < 2):
        return L
    else:
        mid = len(L)//2
        left = mergesort(L[:mid])
        right = mergesort(L[mid:])
        return merge(left, right)

def radixsort(L):
    # Only works for lists of non-negative integers!
    maxValue = max(L)
    def rsort(L, digitSelector):
        if (digitSelector > maxValue):
            return L
        else:
            zeroes = [x for x in L if (x & digitSelector == 0)]
            ones = [x for x in L if (x & digitSelector != 0)]
            return rsort(zeroes + ones, digitSelector<<1)
    return rsort(L, 1)

def callWithLargeStack(f,*args):
    import sys
    import threading
    threading.stack_size(2**27)  # 64MB stack
    sys.setrecursionlimit(2**27) # will hit 64MB stack limit first
    # need new thread to get the redefined stack size
    def wrappedFn(resultWrapper): resultWrapper[0] = f(*args)
    resultWrapper = [None]
    #thread = threading.Thread(target=f, args=args)
    thread = threading.Thread(target=wrappedFn, args=[resultWrapper])
    thread.start()
    thread.join()
    return resultWrapper[0]

def testSort(sortFn, n):
    maxValueInList = 2**30
    L0 = [random.randint(0,maxValueInList) for item in range(n)]
    L = copy.copy(L0)
    startTime = time.clock()
    # result = sortFn(L) # have to callWithLargeStack...
    result = callWithLargeStack(sortFn,L)
    if (result != None):
        # sort was non-destructive, so assign sorted list back into L
        L = result
    elapsedTime = time.clock() - startTime
    assert(L == sorted(L0))
    print("%13s n=%6d  time=%6.3fs" % (sortFn.__name__, n, elapsedTime))

def testSorts():
    n = 2**12
    sortFns = [
                selectionsort,
                insertionsort,
                mergesort,
                quicksort,
                radixsort,
                sorted
              ]
    for sortFn in sortFns:
        testSort(sortFn, n)

testSorts()