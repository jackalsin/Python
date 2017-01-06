# guess 
a = [[1,2], [3,4]]
b = a
# a = a + [7]
a += [7]
print(a,b)

a = {3: 4, 4:5}
print(len(a))


############################## before free response

def longestAnagramList(L, prevWord = None):
    if (L == []):
        return L
    else:
        bestAnagramList = []
        for i in range(len(L)):
            if isLegal(word, prevWord):
                newL = L[:i] + L[i:]
                soln = [word] + longestAnagramList(newL, word)
                if soln != None and len(soln) > len(bestAnagramList):
                    bestAnagramList = soln

        return bestAnagramList

def isLegal(word, prevWord):
    if prevWord == None:
        return True
    else:
        for c in word:
            if c not in prevWord:
                return False
        return True
