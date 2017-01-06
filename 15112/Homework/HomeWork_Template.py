#Homework Exercise 3!!!! Name: Zhiwei Xin Andrew ID: zxin





######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################
def testNearestBusStop():
    print("Testing nearestBusStop()...", end="")
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(4) == 0)
    assert(nearestBusStop(5) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    assert(nearestBusStop(20) == 16)
    assert(nearestBusStop(21) == 24)
    print("Passed. (Add more tests to be more sure!)")