def pittsburghHour(londonHour):
    PIT_24hrs=londonHour-5
    return (PIT_24hrs%12) if PIT_24hrs%12 else 12
def testPittsburghHour():
    print("Testing pittsburghHour()...", end="")

                                     # London   Pittsburgh
    assert(pittsburghHour( 0) ==  7) # midnight    7pm
    assert(pittsburghHour( 5) == 12) #   5am      12am (midnight)
    assert(pittsburghHour(10) ==  5) #  10am       5am
    assert(pittsburghHour(12) ==  7) #  noon       7am
    assert(pittsburghHour(17) == 12) #   5pm       12pm (noon)
    assert(pittsburghHour(18) ==  1) #   6pm       1pm
    print("Passed.")
    print("(Add more tests to be more sure!)")

testPittsburghHour()
