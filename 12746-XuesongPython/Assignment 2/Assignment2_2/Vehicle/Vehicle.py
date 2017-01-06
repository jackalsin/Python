class Vehicle(object):
    def __init__(self, id, height, speed, CurrentNetworkComponent=""):
        self.id = id
        self.height = height
        self.speed = speed
        self.CurrentNetworkComponent = CurrentNetworkComponent

    def time_on_road(self, road):
        if (road.checkHeightLimit(self) or road.checkWeightLimit(self)
                or road.checkSpeedLimit(self)):
            return -1
        else:
            return float(road.length) / float(self.speed)