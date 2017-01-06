
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
assert(str(p1) == ( """Playlist: A Lot Like Christmas
Songs: {Song Title: Sleigh Ride, Artist: Ella Fitzgerald} Current Song: None"""))
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
assert(len(p1.getSongs()) == 4)

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