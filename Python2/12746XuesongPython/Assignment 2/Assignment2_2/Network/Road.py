from Network import Network


class Road(Network):

    def __init__(self):
        super(Road, self).__init__()
        self.ID = 0
        self.current_vehicle_volume = 0
        self.Intersection_1 = ""
        self.Intersection_2 = ""
        self.length = 0

        self.speed_limit = 0
        self.height_limit = 0
        self.weight_limit = 0

    def checkSpeedLimit(self, car):
        if car.speed > self.speed_limit:
            return True
        else:
            return False

    def checkWeightLimit(self, car):
        return car.weight > self.weight_limit

    def checkHeightLimit(self, car):
        return car.height > self.height_limit
