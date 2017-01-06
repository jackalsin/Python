from sklearn import svm
import numpy as np

path = "currentStateFinal.txt"
f = open('data.txt','w')
dataFile = open(path, 'r')
n = 0

# Magic numbers
occupiedSet = [[22, 19, 37], [22, 39, 36], [24, 5, 15], [25, 19, 21], [25, 24, 14]]
emptySet = [[22, 38, 6], [23, 41, 58], [25, 18, 45], [25, 20, 19], [25, 26, 5]]

svmData = []
y = []
queue = []
queueSize = 15

t = 10; #tolerance
def isOccupied(time):
    occupiedSet = [[22, 19, 37-t], [22, 39, 36-t], [24,  5, 15-t], [25, 19, 21-t], [25, 24, 14-t]]
    emptySet    = [[22, 38,  6+t], [23, 41, 58+t], [25, 18, 45+t], [25, 20, 19+t], [25, 26,  5+t]]
    for i in range(5):
        if (time > occupiedSet[i] and time < emptySet[i]):
            return 1
    return 0


for line in dataFile:
    # Date line, ignore " " before line
    if (n % 2 == 0):
        result = []
        currLine = line[1:]
        datas = currLine.split(" ")
        if (len(datas) < 5):
            break
        time = datas[3].split(":")
        hour = time[0]
        minute = time[1]
        second = time[2]
        if (int(hour) < 20):
            hour = int(hour) + 24
        if (isOccupied([int(hour), int(minute), int(second)])):
            #Occupied
            result = 0
        else:
            #Empty
            result = 50
    # Sensor line, ignore PIR sensor version
    else:
        currLine = line[1:]
        distance = currLine.split(" ")[1]
        y.append(result)
        svmData.append([int(distance)])
        if (len(queue) == queueSize):
            queue.pop(0)
        queue.append(int(distance[:-1]))

        f.write(str(round(sum(queue) / len(queue))) + "," + str(result) + "\n")
        
    n += 1
f.close()
dataFile.close()
#print(svmData)
#print(len(svmData))
#print(y)

#clf = svm.SVC(kernel='poly', degree=2, C=1.0)
clf = svm.SVC()

clf.fit(svmData, y)
for i in range(200, 500):
    print(clf.predict([i]))

