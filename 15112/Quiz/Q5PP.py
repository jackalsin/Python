def lockerRoom(lockers):
    lockers=[False] *(lockers+1)
    students=lockers
    openLockers=[]
    for student in range(1,students):
        for locker in range(1,lockers,student):
            lockers[lockers]=not lockers[locker]

    for locker in range(1,lockers):
        if lockers[locker] == True:
            openLockers.append(lockers[locker])
    return openLockers

def merge(a,start1,start2,end):
    index1=start1
    index2=start2
    length=end-start1
    aux=[None]*length
    for i in range (length):
        if ((index1==start2) or (index2 != end and a[index1]>a[index2])):
            aux[i]=a[index2]
            index2+=1
        else:
            aux[i]=a[index1]
            index1+=1
    for i in range (start1,end):
        a[i]=aux[i-start1]
def mergeSort(a)