# Homework 1 Practice
#1.isLegalTriangle(s1, s2, s3)
def isLegalTriangle(s1, s2, s3):
  #return s1>0 and s2>0 and s3>0 and (s1+s2>s3) and (s2+s3>s1) and (s1+s3>s2)
  return (s1>0) & (s2>0) & (s3>0) & (s1+s2>s3) & (s2+s3>s1) & (s1+s3>s2)
  #return s1>0  &  s2>0 & s3>0 & (s1+s2>s3) & (s2+s3>s1) & (s1+s3>s2)

    
      

def testIsLegalTriangle():
    print("Testing isLegalTriangle()...", end="")
    assert(isLegalTriangle(3, 4, 5))
    assert(isLegalTriangle(5, 4, 3))
    assert(isLegalTriangle(3, 5, 4))
    assert(isLegalTriangle(0.3, 0.4, 0.5))
    assert(not isLegalTriangle(3, 4, 7))
    assert(not isLegalTriangle(7, 4, 3))
    assert(not isLegalTriangle(3, 7, 4))
    assert(not isLegalTriangle(5, -3, 1))
    assert(not isLegalTriangle(-3, -4, -5))
    print("Passed.")
    print("(Add more tests to be more sure!)")

testIsLegalTriangle()
