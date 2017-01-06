import math

def sphereVolumeFromSurfaceArea(surfaceArea):
    r=(surfaceArea/4/math.pi)**0.5
    return 4/3*math.pi*r**3 # replace with your solution

def almostEqual(d1, d2):
    epsilon = 10**-4
    return (abs(d1 - d2) < epsilon)

def testSphereVolumeFromSurfaceArea():
    print("Testing sphereVolumeFromSurfaceArea()...", end="")
    # From http://www.aqua-calc.com/calculate/volume-sphere, with r=3, we see:
    assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  904.77868) == True) # r=6
    assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113.09734) == True) # r=3
    assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  904) == False) # r=6
    assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  905) == False) # r=6
    assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113) == False) # r=3
    assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113.1) == False) # r=3
    print("Passed.")
    print("(Add more tests to be more sure!)")

testSphereVolumeFromSurfaceArea()
