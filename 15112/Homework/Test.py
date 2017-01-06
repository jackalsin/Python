def test():
    for i in range(10):
        if i % 2 == 0:
            print("we are here i = ", i)
            continue
    print("outside")
test()