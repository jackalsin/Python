#Run in Python 2.7
import serial
import time
import os
def getPrevDirMap():
    dirMap = set()
    # home = os.path.expanduser("~") + "/dev"
    home = "/dev"
    for dirName in os.listdir(home):
        dirMap.add(dirName)
    return dirMap

def findDirName(prevMap):
    # home = os.path.expanduser("~") + "/dev"
    home = "/dev"
    for dirName in os.listdir(home):
        if ((not dirName in prevMap) and (dirName.startswith("tty"))):
            print dirName
            return ("/dev/" + dirName)

def main():
    prevDirMap = getPrevDirMap()
    str = input("-->")
    dirName = findDirName(prevDirMap)
    print dirName
    ser = serial.Serial(dirName, 9600)
    print "Run..."
    print time.asctime( time.localtime(time.time()))
    
    while(1):
        print ser.readline()
        print time.asctime( time.localtime(time.time()))
    return
main()
