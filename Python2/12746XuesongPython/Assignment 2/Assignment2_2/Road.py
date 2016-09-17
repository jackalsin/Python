class Road():
    ID = 0
    Intersection_1 = ""
    Intersection_2 = ""
    current_vehicle_volume = 0
    length =0

    speed_limit=0
    height_limit=0
    weight_limi=0

    def checkSpeedLimit(self, car):
        if car.speed > self.speed_limit:
            return True
        else:
            return False


    def checkWeightLimit(self, car):


    def checkHeightLimit(self, car):

