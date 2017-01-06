# recursion Advanced

# 
def powerset(a):
    if (len(a) == 0):
        return [[]]
    else:
        otherSet = powerset(a[1:])
        result = []
        for other in otherSet:
            result.append(other + [a[0]])
        return otherSet + result

print(sorted(powerset([1,2,3])))

def permutation(l):
    if len(l) == 0:
        return [[]]
    else:
        result = []
        for subpermutation in permutation(l[1:]):
            for i in range(len(subpermutation) + 1):
                result += [subpermutation[:i] + [l[0]] + subpermutation[i:]]
        return result

print(permutation([1,2,3]))

import os
def printFiles(path):
    if os.path.isdir(path) == False:
        print(path)
        return
    else:
        for sub in os.listdir(path):
            printFiles(path + "/" + sub)

printFiles("sampleFiles")