import random
def randomRunLength():
    lenSum = 0
    trails = 1000000000000
    for i in range(trails):
        aList =[]
        while True:
            newNum = random.random()
            if aList == []:
                aList.append(newNum)
            else:
                if aList[-1]>newNum:
                    aList.append(newNum)
                else:
                    lenSum += len(aList) + 1
                    break

    return lenSum/trails

print(randomRunLength())