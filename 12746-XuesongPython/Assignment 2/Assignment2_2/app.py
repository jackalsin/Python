from Network.Intersection import Intersection
from Vehicle.Truck import Truck

from Network.Road import Road
from Vehicle.Car import Car


def main():
    roadA = Road()
    initRoad(roadA, 300, 35, float("inf"), 13.5)
    roadB = Road()
    initRoad(roadB, 90, 25, 10, float("inf"))
    roadC = Road()
    initRoad(roadC, 90, 25, 10, float("inf"))
    roadD = Road()
    initRoad(roadD, 155, 15, float("inf"), float("inf"))
    roadE = Road()
    initRoad(roadE, 160, 15, float("inf"), 10)
    # init intersection
    intersection1 = Intersection()
    intersection1.ID = 1
    # assign intersection
    for child in [roadA, roadB, roadC, roadD, roadE]:
        child.intersection1 = intersection1.ID

    carOne = Car(1, 5, 24)
    carTwo = Car(2, 5.1, 40)

    truckOne = Truck(1, 11.3, 3, 14)


def initRoad(road, length, speedLimit, weightLimit, heightLimit):
    road.length = length
    road.speed_limit = speedLimit
    road.weight_limit = weightLimit
    road.height_limit = heightLimit


if __name__ == '__main__':
    main()
