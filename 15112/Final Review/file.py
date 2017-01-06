import copy
def transpose(triple):
    (rows, cols, L) = triple
    print(rows, cols)
    newL = []
    for col in range(cols):
        for row in range(rows):
            index = row * cols + row
            print(row, col, index)
            newL.append(L[row * cols + col])
    print(newL)
    return (cols, rows, newL)

def testTranspose():
    triple = (2,3,[5, 8, 1, 0, 7, 4])
    assert(transpose(triple) == (3, 2, [5, 0, 8, 7, 1, 4]))

testTranspose()

def bestConnection(cvs, fromCity, toCity):
    cityDir = getCityDir(cvs)

    costDir = cityDir[fromCity]
    bestConnCost = None
    bestConnCity = None
    for connCity in costDir:
        if connCity == toCity:
            directCost = costDir[toCity]
        else:
            toConnCost = costDir[connCity]
            toCityCost = cityDir[connCity][toCity]
            indirCost = int(toConnCost )+ int(toCityCost)
            if bestConnCost == None:
                bestConnCost = indirCost
                bestConnCity = connCity
            elif bestConnCost > indirCost:
                bestConnCost = indirCost
                bestConnCity = connCity
    print((bestConnCity, directCost, bestConnCost))
    return(bestConnCity, directCost, bestConnCost)

def getCityDir(cvs):
    d = dict()
    for line in cvs.split("\n"):
        L = line.split(",")
        
        d[L[0]] = {}

        for i in range(1, len(L),2):
            d[L[0]][L[i]] = L[i+1]
    return d


def testBestConne():
    CSV = """boston,new york,280,pittsburgh,120,chicago,325
new york,pittsburgh,220,chicago,340,boston,220
pittsburgh,chicago,190,boston,80,new york,150
chicago,boston,100,new york,120, pittsburgh,75"""

    bestConnection(CSV, "boston", "new york")

testBestConne()


def longestAnagramList(L, prevWord = None):
    if (L == []):
        return L
    else:
        bestList = []
        
        for word in L:
            newL = copy.copy(L)
            newL.remove(word)
            if isAna(prevWord, word):
                result = longestAnagramList(newL,word)
                if result != None:
                    result = [word] + result
                    if (len(result) > len(bestList)):
                        bestList = result
        
        return bestList

def isAna(prevWord, word):
    if prevWord == None:
        return True

    else:
        count = 0
        for c in word:
            if c not in prevWord:
                return False
            else:
                count += 1
        if count == len(prevWord) - 1:
            return True
        else:
            return False


def testLongestAn():
    L = ["abcd", "dca", "ca", "bac", "ba", "b"]
    assert(longestAnagramList([]) == [])
    assert(longestAnagramList(["abcd", "bcl"]) == ["abcd"])
    assert(longestAnagramList(["xyzw","mzw","zw","z"])==["mzw","zw", "z"]) 
    assert(longestAnagramList(["xyzw", "mzl", "zw", "z"])== ["zw", "z"])\

testLongestAn()