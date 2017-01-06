# sort recursive
L = [3,5,6,7,7,8,33,23,5]
def insertionSort(L):
    if (len(L) == 0):
        return []
    else:
        pivot = L[0]
        rest = (L[1:])
        left = [x for x in rest if x < L[0]]
        right = [x for x in rest if x >= L[0]]
        return insertionSort(left) + [pivot] + insertionSort(right)

print(insertionSort(L))


def merge(left, right):
    if (len(left) == 0 or len(right) == 0):
        return left + right
    elif left[0] < right[0]:
        return [left[0]] + merge(left[1:],right)
    elif left[0] >= right[0]:
        return [right[0]] + merge(left, right[1:])


def mergeSort(L):
    if (len(L) == 1):
        return L
    else:
        mid = len(L)//2
        left = mergeSort(L[:mid])
        right = mergeSort(L[mid:])
        return merge(left,right)

print(mergeSort(L))
print(L)

def quickSort(L):
    if (len(L) == 0):
        return []

    else:
        pivot = L[0]
        rest = L[1:]
        left = [x for x in rest if x < pivot]
        right = [x for x in rest if x >= pivot]

        return quickSort(left) + [pivot] + quickSort(right)

print(quickSort(L))