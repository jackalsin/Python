def mergeSort(L):
    n = len(L)
    step = 1
    start1 = 0
    while (step < n):
        for start1 in range(0, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2 * step, n) 
            print(start1, start2, end)
            merge(L,start1,start2,end)
        step *= 2
    return L

def merge(L,start1, start2,end):
    aux = [None] * (end - start1)
    j = start1
    k = 0
    while (k < (len(aux))):
        if (start2 >= end or (start1 < start2 and L[start1] < L[start2])):
            aux[k] = L[start1]
            start1 += 1
        else:
            aux[k] = L[start2]
            start2 += 1
        k += 1
    print(aux)
    for i in range(len(aux)):
        L[j] = aux[i]
        j+=1

    return L

L = [1,35,2,1,34,5,4,2,7,3]
mergeSort(L)
# print(mergeSort(L))

print(L)

import random


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def selectionSort(a):
    for i in range(len(a)):
        minIndex = i
        for j in range(i, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
        print(i, minIndex)
        swap(a,i,minIndex)


L = [1,35,2,1,34,5,4,2,7,3]


selectionSort(L)


def bubbleSort(a):
    i = 0
    end = len(a)
    while (end > 0):
        for j in range(end - 1):
            if a[j] > a[j+1]:
                swap(a, j, j + 1)    
        end -= 1 


L = [1,35,2,1,34,5,4,2,7,3]


bubbleSort(L)
print(L)