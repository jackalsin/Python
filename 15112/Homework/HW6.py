###### Spring 2014 Quiz 1 
"""it can't run"""
""""(d2,d1)=-10,-12   it needs absolute values"""
"""
A 12
B 49
C 1
D 1.6
E 1.0
F 3
G 1
H 2
I True
J False
M 1
N <class 'int'>
O None
"""

"""64"""

"""def runToInt(f):
    return (f+0.5)//1
"""
#### Spring 2014 Quiz 2

"""
(4,4)
(2,6)
(25,7)
(28,44)
"""

"""
(8,5)
(15,6)
(16,8)
"""

"""7"""

"""301"""

"""because f(x)>=0, and the expression f(start)*f(end) will be
always greater than or equal to 0"""

"""def sameDigits(m,n):
    if m == n ==0:
        return True
    else:
        (m,n)=(max(m,n),min(m,n))
    while(m):
        nOrignal=n
        while(n):
            if n%10==m%10:
                break
            n//=10
        if n ==0:return False
        m//=10
    return True"""

import copy
# bigO Better Big Oh [20 pts] 

"""
slow1:
count the number of elements
O(n)

def slow1(a):
    return len(a)

it's O(1)


slow2:
to check if there is identical elements
it's O(n^2)
def slow2(a):
    aSet=set(a)
    return len(aSet) == len(a)

it's O(1)


slow3:
to return sum of elements in list b but not in list b
it's O(n^2)

def slow33(a,b):
    (aSet,bSet)=(set(a),set(b))
    dif=bSet.difference(a)
    result=0
    bDict=dict()
    for item in b:
        if item not in bDict:
            bDict[item]=0
        bDict[item]+=1
    for item in dif:
        result+=bDict[item]
    return result

it's O(n). It is resulted from the two independent for loop


slow4:
to return the largest absolute difference between elements in list a and list b
it's O(n^2)

def slow44(a,b):
    (amax,amin,bmax,bmin)=(max(a),min(a),max(b),min(b))
    possibleValue2=bmax-amin
    possibleValue1=amax-bmin
    return max(abs(possibleValue1),abs(possibleValue2))

it's O(NlogN)
though I used the max, actually it only compares once. Therefore, bigO is 
decided by max(), which is N

slow5:
to find the least absolute difference between an element in a 
and another element in b

it't O(N^2) there is nested loops, 

import bisect
def slow55(a,b):
    a.sort()
    bestDif=a[0]-b[0]
    b=set(b)
    aLen=len(a)
    for item in b:
        position=bisect.bisect(a,item)
        curtNum=a[position%aLen]
        prevNum=a[(position-1)%aLen]
        nextNum=a[(position+1)%aLen]
        bestDif=min(bestDif,abs(item-prevNum),abs(item-nextNum),abs(item-curtNum))
    return bestDif

the bigO in this case will be o(NlogN), which is from sort

"""

# invertDictionary

def invertDictionary(d):
    invD=dict()
    for key in d:
        (newKey,newValue)=(d[key],key)
        if newKey not in invD:
            invD[newKey]=[newValue]
        else:
            invD[newKey].append(newValue)
    for key in invD:
        invD[key]=set(invD[key])
    return invD



# 4.sparseMatrixAdd(sm1, sm2):[20 pts] 
def sparseMatrixAdd(sm1, sm2):
    sm3=copy.deepcopy(sm2)
    for key in sm1:
        if key == "rows":
            sm3[key]=max(sm1["rows"],sm2["rows"])
        elif key == "cols":
            sm3[key]=max(sm1["cols"],sm2["cols"])
        elif key in sm3:
            sm3[key]+=sm1[key]
        else:
            sm3[key]=sm1[key]
    return sm3

def friendsOfFriends(d):
    fof=dict()
    for owner in d: # find Fred
        print()
        print("Now we are testing", owner)
        fof[owner]=set() # Creat for convience
        for guest in d: # get wilma
            print("Now we are testing", guest)
            if guest == owner:
                continue
            sumFriend=d[owner].union(d[guest])-set([owner,guest]) 
            # remove themselves
            print("sumFriend", sumFriend)
            addName=sumFriend-d[owner]
            print("addName",addName) 
            # remove direct friends
            fof[owner]=fof[owner].union(addName)
    return fof

print(friendsOfFriends({'barney': set(), 'betty': set(), 'bam-bam': set(), 'wilma': {'betty', 'fred', 'dino'}, 'fred': {'barney', 'wilma', 'betty', 'bam-bam'}, 'dino': set()}))



def testFriendsOfFriends():
    d=dict()
    d["fred"] = set(["wilma", "betty", "barney", "bam-bam"])
    d["wilma"] = set(["fred", "betty", "dino"]) ###
    d['betty'] = set(["wilma", "fred"])
    d["barney"] = set(["fred"])
    d["dino"] = set(["wilma"]) #####
    d["bam-bam"] = set(['fred'])
    fofReturn=friendsOfFriends(d)
    print("Test of invertDictionary()...",end=" ")
    assert(fofReturn["fred"]==set(["dino"]))
    assert(fofReturn["wilma"] == set(["barney", "bam-bam"]))
    print("passed")

def testSparseMatrixAdd():
    print("Test of sparseMatrixAdd()...",end=" ")
    assert(sparseMatrixAdd({"rows":5, "cols":4, (1,1):2, (1,2):3},
                       {"rows":3, "cols":6, (1,1):5, (2,2):6}) ==
                       {"rows":5, "cols":6, (1,1):7, (1,2):3, (2,2):6})
    assert(sparseMatrixAdd({"rows":0, "cols":0},
                       {"rows":3, "cols":6, (1,1):5, (2,2):6}) ==
                       {"rows":3, "cols":6, (1,1):5, (2,2):6})
    print("passed")

def testInvertDictionary():
    print("Test of invertDictionary()...",end=" ")
    assert(invertDictionary({1:2, 2:3, 3:4, 5:3}) == 
       {2:set([1]), 3:set([2,5]), 4:set([3])})
    assert(invertDictionary({}) == {})
    assert(invertDictionary({2:3}) == {3:set([2])})
    print("passed")

def testAll():
    testInvertDictionary()
    testSparseMatrixAdd()
    # testFriendsOfFriends()


testAll()