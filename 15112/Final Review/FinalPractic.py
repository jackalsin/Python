CSV = """boston,new york,280,pittsburgh,120,chicago,325
new york,pittsburgh,220,chicago,340,boston,220
pittsburgh,chicago,190,boston,80,new york,150
chicago,boston,100,new york,120, pittsburgh,75"""

def bestConnection(costCSV, fromCity, toCity):
    # split 
    csvList = []
    for line in costCSV.splitlines():
        temp = []
        for word in line.split(","):
            temp.append(word)
        csvList.append(temp)

    for i in range(len(csvList)):
        if toCity == csvList[i][0]:
            getFromCity = csvList[i]

    if toCity not in getFromCity:
        return
    # get Direct
    for i in range(len(getFromCity)):
        if toCity == getFromCity[i]:
            nonStopCost = getFromCity[i+1]

    # recursion
    bestCity = None
    bestCost = None
    for i in range(1, len(getFromCity),2):
        if toCity != getFromCity[i]:
            result = bestConnection(costCSV,getFromCity[i], toCity)
            if result == None: 
                return None
            else:
                curConectCost = int(result[2]) + int(getFromCity[i+1])
            if bestCost == None:
                bestCost = curConectCost
                bestCity = getFromCity[i]
            else:
                if bestCost > curConectCost:
                    bestCost = curConectCost
                    bestCost = getFromCity[i]

    return (bestCost, nonStopCost, curConectCost)


import math
print(math.cos(3))



class HolidaySong(object):
    """docstring for HolidaySong"""
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist        

    def __repr__(self):
        return "Song Title: %s, Artist: %s" % (self.title, self.artist)

    def __eq__(self, other):
        return (isinstance(other, HolidaySong) and 
            (self.title == other.title) and (self.artist == other.artist))

class SleighRide(HolidaySong):
    """docstring for SleighRide"""
    def __init__(self, artist):
        titleStr = "Sleigh Ride"
        super(SleighRide, self).__init__(titleStr, artist)


class HolidayPlaylist(object):
    """docstring for HolidayPlaylist"""
    def __init__(self, title):
        self.title = title
        self.playList = []
        self.currentSong = None
        self.curIndex = -1

    def playNextSong(self):
        if (self.playList == []):
            return "No songs yet."
        else:
            curName = None
            if self.currentSong != None:
                curName = self.currentSong.title
            while (True):
                self.curIndex += 1
                if (self.curIndex >= len(self.playList) and 
                                        curName != self.playList[-1]):
                    return "Playlist done."
                self.currentSong = self.playList[self.curIndex]
                if (self.currentSong.title == curName):
                    if (self.curIndex + 1 == len(self.playList)):
                        return "Playing."
                    continue
                else:
                    break
            return "Playing."
        # if (self.curIndex + 1 > len(self.playList)):
            # return 
    def getCurrentSong(self):
        return self.currentSong

    def addSong(self, song):
        self.playList.append(song)

    def __repr__ (self):
        content = ("{Song Title: %s, Artist: %s}" % 
                    (self.playList[0].title, self.playList[0].artist))
        
        result = (("""Playlist: %s Songs: %s Current Song: %s""") % (self.title, content, self.currentSong))
        return result

    def getSongs(self):
        return self.playList
# test Case
song0 = HolidaySong("Silent Night", "Michael Buble")
song1 = HolidaySong("Silent Night", "Michael Buble") 

assert(song1.title == "Silent Night" and song1.artist == "Michael Buble") 
assert(str(song1) == "Song Title: Silent Night, Artist: Michael Buble") 
song2 = HolidaySong("Do They Know It's Christmas", "Band­Aid") 
assert (song1 == song0) # same title and artist 
assert (song1 != song2)
song3 = SleighRide("Ella Fitzgerald") 
assert(isinstance(song3, HolidaySong)) 
assert(str(song3) == "Song Title: Sleigh Ride, Artist: Ella Fitzgerald") 
song4 = SleighRide("Pentatonix") 
assert(str(song4) == "Song Title: Sleigh Ride, Artist: Pentatonix") 
assert(song3 != song4) # still not equal! 
assert(song3 != "White Christmas") # does not crash!

p1 = HolidayPlaylist("A Lot Like Christmas") 
assert(p1.playNextSong() == "No songs yet.") 
assert(p1.getCurrentSong() == None)
p1.addSong(song3)
assert(str(p1) == ( """Playlist: A Lot Like Christmas Songs: {Song Title: Sleigh Ride, Artist: Ella Fitzgerald} Current Song: None"""))
assert(p1.playNextSong() == "Playing.") 
assert(p1.getCurrentSong() == song3) 
assert(len(p1.getSongs()) == 1)
p1.addSong(song4)
p1.addSong(song1) 
p1.addSong(song2)
p1.addSong(song0)
assert(song4 in p1.getSongs()) 
assert(song1 in p1.getSongs()) 
assert(song2 in p1.getSongs()) 
assert(len(p1.getSongs()) == 5)

assert(p1.playNextSong() == "Playing.") # When selecting next song, choose one that does not have the same title! 
assert(p1.getCurrentSong() != song4) 
p1.playNextSong() 
p1.playNextSong() 
assert(p1.playNextSong() == "Playlist done.")

p2 = HolidayPlaylist("Chesnuts Roasting") 
p2.addSong(song3) 
assert(p2.playNextSong() == "Playing.") 
assert(p2.getCurrentSong() == song3) 
p2.addSong(song4)
assert(p2.playNextSong() == "Playing.") # Still play next song even if the same title, since there's nothing else! 
assert(p2.getCurrentSong() == song4) 
assert(p2.playNextSong() == "Playlist done.")
print('passed')