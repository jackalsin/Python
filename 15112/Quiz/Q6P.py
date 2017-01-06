def mostCommonName(L):
    nameDict=dict()
    bsetCount=0
    bestName=[]
    for name in L:
        if name in nameDict:
            nameDict[name]+=1
        else:
            nameDict[name]=1
    for key in nameDict:
        if nameDict[key]>bsetCount:
            bestName=key
            bsetCount=nameDict[key]
        elif nameDict[key]==bsetCount:
            if type(bestName)!=list:
                bestName=[bestName]
            print(nameDict[key])
            bestName.append(key) 
    return bestName if bestName!=[] else None# place your answer here!

def mostCommonName2(L):
    # use list
    bestName=set()
    bestCount=0
    for name in L:
        currentCount=0
        if currentCount > bestCount:
            bestName=name
            bestCount=currentCount
        elif currentCount ==  bestCount:
            bestName.add(name)
    return list(bestName)
def testMostCommonName():
    print("Testing mostCommonName()...", end="")
    assert(mostCommonName(["Jane", "Aaron", "Cindy", "Aaron"])
           == "Aaron")
    assert(sorted(mostCommonName(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]))
           == ["Aaron", "Jane"])
    assert(mostCommonName(["Cindy"]) == "Cindy")
    assert(sorted(mostCommonName(["Jane", "Aaron", "Cindy"]))
           == ["Aaron", "Cindy", "Jane"])
    assert(mostCommonName([]) == None)
    print("Passed!")

testMostCommonName()
def testMostCommonName2():
    print("Testing mostCommonName2()...", end="")
    assert(mostCommonName2(["Jane", "Aaron", "Cindy", "Aaron"])
           == "Aaron")
    assert(sorted(mostCommonName2(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]))
           == ["Aaron", "Jane"])
    assert(mostCommonName2(["Cindy"]) == "Cindy")
    assert(sorted(mostCommonName2(["Jane", "Aaron", "Cindy"]))
           == ["Aaron", "Cindy", "Jane"])
    assert(mostCommonName2([]) == None)
    print("Passed!")

testMostCommonName2()