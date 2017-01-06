# the Locker Room
def lockerProblem(lockers):
    lockersOpen=[False]*(lockers+1)
    students=lockers
    for student in range (1,students+1):
        for locker in range(student,lockers+1,student):
            lockersOpen[locker] = not lockersOpen[locker]
    openNumbers=[]
    for locker in range (1,lockers+1):
        if lockersOpen[locker]==True:
            openNumbers+=[locker]
    return openNumbers

print(lockerProblem(2000))



# anagams

def isAnagram(s1,s2):
    if sorted(s1.lower()) == sorted(s2.lower()):
        return True
    else:
        return False


def testIsAnagram():
    print("Testing isAnagram()...", end="")
    assert(isAnagram("", "") == True)
    assert(isAnagram("abCdabCd", "abcdabcd") == True)
    assert(isAnagram("abcdaBcD", "AAbbcddc") == True)
    assert(isAnagram("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")

testIsAnagram()


def sieve(n):
    L=[True]*(n+1)
    L[0]=L[1]=False
    prime=[]
    for i in range(2,len(L)):
        for j in range (i,len(L),i):
            if j!=i:
                L[j]=False
    for i in range (len(L)):
        if L[i]==True:
            prime.append(i)
    return prime
print(sieve(50))


def swap(l,i,j):
    l[i],l[j]=l[j],l[i]

def selectionSort(a):
    for startIndex in range(len(a)):
        minIndex=startIndex
        for checkIndex in range(startIndex,len(a)):
            if a[minIndex] > a[checkIndex]:
                swap(a,minIndex,checkIndex)
L=[12,2542,763,145,2,13,5,76,4]
print(L)
selectionSort(L)
print(L)

def merge(a, start1,start2,end):
    length=(end-start1)
    auxiliary = length*[None]
    index1=start1
    index2=start2
    print("length,index1,index2", length,index1,index2,end)

    for i in range(start1,end):
        print("we are evaluating i= ",i,end)
        print("index1,index2",index1,index2)
        print("auxiliary=",auxiliary)
        # print("a[index1,index2",a[index1],a[index2])
        if index2==end:
            # auxiliary+=a[index1+1:start2]
            auxiliary[i-start1]=a[index1]
            index1+=1
        elif index1==start2:
            # auxiliary+=a[index2+1:end]
            auxiliary[i-start1]=a[index2]
            index2+=1
        elif a[index1]<a[index2]:
            print("i and index1",i, index1)
            auxiliary[i-start1]=a[index1]
            index1+=1
        elif a[index1] >=a[index2]:
            auxiliary[i-start1]=a[index2]
            index2+=1
        print(auxiliary)
    for i in range(length):
        a[start1+i]=auxiliary[i]


def mergeSort(a):
    start1=start2=0
    step=1
    n=len(a)
    while (step<n):
        for start1 in range (0,len(a),2*step):
            start2=min(start1+step,n)
            end=min(start1+2*step,n)
            merge(a,start1,start2,end)
        step*=2
a=[8,7,6,5,4,3,2,1]
mergeSort(a)
print(a)