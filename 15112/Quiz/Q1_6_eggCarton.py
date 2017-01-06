#eggCartons
def eggCartons(eggs):
    return eggs//12+1 if eggs%12!=0 else eggs//12

def testEggCartons():
    print("Testing eggCartons()...", end="")
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testEggCartons()


