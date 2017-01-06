def rc2(L):
    (rows,cols) = (len(L),len(L[0]))
    d = {0:0}
    for row in range(rows):
        for col in range(cols):
            key = L[row][col]
            if key == 0:
                d[0]+=1
                # print("we are adding 1 Row %d, Col %d" % (row,col))
            else:
                d[key]=10*row + col
    return (d ) #== {0:5,42:11,13:2})

# print(rc2([[13,0,13],[42,42,0],[0,0,0]]))
import time

def bigOh3(n):
    j = 5
    while (j**2<n):
        j+=3

def test():
    n = 10000000000000
    start1 = time.time()
    bigOh3(n)
    end1=time.time()
    during1 = end1 - start1
    start2 = time.time()
    bigOh3(2*n)
    end2 = time.time()
    during2 = end2- start2
    ratio = during2/during1
    print(ratio)
test()