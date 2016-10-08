from Assignment2_2.Vehicle.Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, ID="", height="", speed=0, CurrentNetworkComponent=""):
        super(Car, self).__init__(ID, height, speed, CurrentNetworkComponent)

    def time_on_road(self, road):
        super(Car, self).time_on_road(road)
