import copy

def main():
    a=[[1],[2],[3]]
    b=a
    c=copy.copy(a)
    d=copy.deepcopy(a)
    a[0][0]=42
    a[1]=2
    b[2]=777
    print(a)
    print(b)
    print(c)
    print(d)

main()