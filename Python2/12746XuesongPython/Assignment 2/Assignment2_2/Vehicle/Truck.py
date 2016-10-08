from Vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, ID="", height="", weight=0, speed=0, CurrentNetworkComponent=""):
        super(Truck, self).__init__(ID, height, speed, CurrentNetworkComponent)
        self.weight = weight

    def time_on_road(self, road):
        if (road.checkHeightLimit(self) or road.checkWeightLimit(self)
                or road.checkSpeedLimit(self)):
            return -1
        else:
            return float(road.length) / float(self.speed)
