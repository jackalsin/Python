import string
def letterCount(c,s):
    count=0
    for i in (s):
        if i==c:
            count+=1
    return count



def mostFrequentLetters(s):
    s=s.upper()
    print(s)
    for i in s
    return best # replace with your answer!

def testMostFrequentLetters():
    print("Testing mostFrequentLetters()...", end="")
    assert(mostFrequentLetters("Cat") == 'ACT')
    assert(mostFrequentLetters("A cat") == 'A')
    assert(mostFrequentLetters("A cat in the hat") == 'AT')
    assert(mostFrequentLetters("This is a test") == 'ST')
    assert(mostFrequentLetters("This is an I test?") == 'IST')
    assert(mostFrequentLetters("") == "")
    print("Passed!")

testMostFrequentLetters()
