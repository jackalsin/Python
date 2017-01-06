# hw2.py
# Zhiwei Xin + zxin + Section AA

import math

def sumOfSquaresOfDigits(n):
    Sum=0
    while n:
        Sum+=(n%10)**2
        n//=10
    return Sum

def isHappyNumber(n):
    if n<1: 
        return False
    else: 
        while (sumOfSquaresOfDigits(n)!=4):
            if sumOfSquaresOfDigits(n)==1:
                return True
            else:
                n=sumOfSquaresOfDigits(n)
        return False
# print(isHappyNumber(16))
      
def nthHappyNumber(n):
    count=0
    guess=0
    while(count<=n):
        guess+=1
        if isHappyNumber(guess):
            count+=1
    return guess
# print(nthHappyNumber(5))
def isPrime(n):
    if n<1: 
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        limit=round(math.sqrt(n)+1)
        for i in range (3,limit,2):
            if n%i==0:
                return False
        return True
# print(isPrime(9))

def nthHappyPrime(n):
    count=0
    guess=0
    while (count<=n):
        guess+=1
        if isHappyNumber(guess) and isPrime(guess):
            count+=1
    return guess

#print(nthHappyPrime(3))
    ############## Question 2
def digitsNumber(n):
    n=abs(n)
    if n ==0: return 1
    count=0
    while n:
        count+=1
        n//=10
    return count
def isKaprekarNumber(n):
    for k in range (digitsNumber(n)):
        square=n**2
        head=square//10**(k+1)
        tail=square%10**(k+1)
        if tail==0:
            continue
        elif head+tail==n:
            return True
    return False
#print(isKaprekarNumber(10))

def nearestKaprekarNumber(n):
    guess=0
    while guess<=n: # get smaller 
        guess+=1
        if isKaprekarNumber(guess):
            smaller=guess
    count = 0
    while count==0:
        guess+=1
        if isKaprekarNumber(guess):
            larger=guess
            count+=1
    if abs(smaller-n)<=abs(larger-n):
        return smaller
    else:
        return larger

#print(nearestKaprekarNumber(26))
def isCarolNumber(n):
    k=0
    while ((2**k - 1)**2 - 2)<=n:
        guess=((2**k - 1)**2 - 2)
        if guess==n:
            return True
        k+=1
    return False

#print(isCarolNumber(3967))
def nthCarolPrime(n):
    k=0
    count=0
    while count<=n:
        guess=(2**k - 1)**2 - 2
        if isPrime(guess):
            count+=1
        k+=1
   # print (guess)
    return guess

########Question 4
def Area(f,a,b):
    left=abs(f(a))
    right=abs(f(b))
    width=(b-a)
    if f(a)*f(b)>=0:
        return 0.5*(left+right)*width
    else:
        leftWidth=(b-a)/(left+right)*left
        rightWidth=(b-a)/(left+right)*right
        leftArea=0.5*leftWidth*left
        rightArea=0.5*rightWidth*right
        #print("leftWidth=",leftWidth,", rightWidth=",rightWidth,",leftArea=",leftArea,",rightArea=",rightArea)
        return leftArea+rightArea

def integral(f, a, b, N): 
    bias=(b-a)/N
    xLeft=a
    xRight=a+bias
    area=0
    while(xRight<=b):
        area+=Area(f,a,b)
        xLeft+=bias
        xRight+=bias
    return area


######Qusetion 5
def kthDigit(n,k):
    n=abs(n)# k=0, output the first right digit
    return (n//10**k)%10

def digitCounts(n):
    n=abs(n)
    if n==0: return 1
    count=0
    while n:
        count+=1
        n//=10
    return count

def singleMultiply(m,n): # n is oneDigits
    k=digitCounts(m)
    product=0
    for i in range(k+1):
        mDigit=kthDigit(m,i)
        product+=mDigit*n%10*(10**i)
        #print(product)
    return product

def carrylessAdd(x,y):
    sum=0
    digits=digitCounts(max(x,y))
    for i in range (digits):
        xKthDigit=kthDigit(x,i)
        yKthDigit=kthDigit(y,i)
        digitSum=(xKthDigit+yKthDigit)%10
        sum+=digitSum*10**i
    return sum

def carrylessMultiply(x,y):
    product=0
    yDigits=digitCounts(y)
    for i in range (yDigits):
        currentYDigits=kthDigit(y,i)
        temp=singleMultiply(x,currentYDigits)
        #print("when i=",i,", the temp=", temp)
        product=carrylessAdd(temp*10**i,product)
    return product

######### Question 6###############
def makeBoard(moves):
    board=8
    for count in range (moves-1):
        board=board*10+8
    #print(board)
    return board

def digitCount(n):
    return digitCounts(n)

def replaceKthDigit(n, k, d):
    return (n+(d-kthDigit(n,k))*10**k)

def getLeftmostDigit(n):
    return(n//(10**(digitCount(n)-1)))

def clearLeftmostDigit(n):
    return ( n-getLeftmostDigit(n)*(10**(digitCount(n)-1)) )

def makeMove(board,position,move):
    #print("the current board is",board,"position is",position,", the move is", move)
    if move!=1 and move!=2:
        #print("move passed")
        return "move must be 1 or 2!"
    elif position>digitCount(board):
        #print("offboard Passed")
        return "offboard!"
    elif kthDigit(board,(digitCount(board)-position))!=8:
        #print("kthDigit")
        return "occupied!"
    else:
        #print("replaceKthDigit")
        #print(replaceKthDigit(board,(digitCount(board)-position),move))
        return (replaceKthDigit(board,(digitCount(board)-position),move))

def isWin(board):
    for k in range (digitCount(board)):
        if (kthDigit(board,k)==2 and 
            kthDigit(board,k+1)==1 and
            kthDigit(board,k+2)==1):
            return True
    return False

def isFull(board):
    for k in range(digitCount(board)):
        if kthDigit(board,k)==8:
            return False
    else:
        return True

def getBoard(game):
    specfic=clearLeftmostDigit(game)
    board=makeBoard(getLeftmostDigit(game))
    for k in range (round(digitCount(specfic)/2)):
        position=getLeftmostDigit(specfic) #this position is left to right
        specfic=clearLeftmostDigit(specfic)
        move=getLeftmostDigit(specfic)
        specfic=clearLeftmostDigit(specfic)
        board=makeMove(board,position,move)
    return board

def getBoardNumber(game):
    specfic=clearLeftmostDigit(game)
    board=makeBoard(getLeftmostDigit(game))
    for k in range (round(digitCount(specfic)/2)):
        position=getLeftmostDigit(specfic) #this position is left to right
        specfic=clearLeftmostDigit(specfic)
        move=getLeftmostDigit(specfic)
        specfic=clearLeftmostDigit(specfic)
        if not type(makeMove(board,position,move))==int:
            #print("now we are printing from subFunction", board)
            return board
        board=makeMove(board,position,move)
    return board

#print(getBoardNumber(523))

def turn(game):
    game=clearLeftmostDigit(game)
    digits=digitCount(game)
    if digits%4==0:
        return 2
    else: 
        return 1
# print(turn(52112315142 ))
def play112(game):
    board=getBoard(game)
    boardNumber=getBoardNumber(game)
    #print(boardNumber)
    #print(board)
    if not (type(board)==int):
        #print (str(boardNumber)+": Player "+str(turn(game))+": "+board)
        return str(boardNumber)+": Player "+str(turn(game))+": "+board
    elif isWin(board):
        return str(board)+": Player "+str(turn(game))+" wins!"
    elif isFull(board):
        #print(str(board)+"Tie!")
        return str(board)+": Tie!"
    else:
        return str(board)+": Unfinished!"
# print(play112(52112315142))
######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def testSumOfSquaresOfDigits():
    print("Testing sumOfSquaresOfDigits()...", end="")
    assert(sumOfSquaresOfDigits(5) == 25)   # 5**2 = 25
    assert(sumOfSquaresOfDigits(12) == 5)   # 1**2 + 2**2 = 1+4 = 5
    assert(sumOfSquaresOfDigits(234) == 29) # 2**2 + 3**2 + 4**2 = 4 + 9 + 16 = 29
    print("Passed. (Add more tests to be more sure!)")

def testIsHappyNumber():
    print("Testing isHappyNumber()...", end="")
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print("Passed. (Add more tests to be more sure!)")

def testNthHappyNumber():
    print("Testing nthHappyNumber()...", end="")
    assert(nthHappyNumber(0) == 1)
    assert(nthHappyNumber(1) == 7)
    assert(nthHappyNumber(2) == 10)
    assert(nthHappyNumber(3) == 13)
    assert(nthHappyNumber(4) == 19)
    assert(nthHappyNumber(5) == 23)
    assert(nthHappyNumber(6) == 28)
    assert(nthHappyNumber(7) == 31)
    print("Passed. (Add more tests to be more sure!)")

def testNthCarolPrime():
    print("Testing nthCarolPrime()...", end="")
    assert(nthCarolPrime(0) == 7)
    assert(nthCarolPrime(1) == 47)
    assert(nthCarolPrime(2) == 223)
    assert(nthCarolPrime(3) == 3967)
    assert(nthCarolPrime(4) == 16127)
    assert(nthCarolPrime(5) == 1046527)
    assert(nthCarolPrime(6) == 16769023)
    print("Passed. (Add more tests to be more sure!)")

def testCarrylessMultiply():
    print("Testing carrylessMultiply()...", end="")
    assert(carrylessMultiply(643,59) == 417)
    # assert(carrylessMultiply(1) == 47)
    # assert(carrylessMultiply(2) == 223)
    # assert(carrylessMultiply(3) == 3967)
    # assert(carrylessMultiply(4) == 16127)
    # assert(carrylessMultiply(5) == 1046527)
    # assert(carrylessMultiply(6) == 16769023)
    print("Passed. (Add more tests to be more sure!)")

def testMakeBoard():
    print("Testing makeBoard()...", end="")
    assert(makeBoard(1) == 8)
    assert(makeBoard(2) == 88)
    assert(makeBoard(3) == 888)
    print("Passed. (Add more tests to be more sure!)")

def testDigitCount():
    print("Testing digitCount()...", end="")
    assert(digitCount(0) == 1)
    assert(digitCount(5) == digitCount(-5) == 1)
    assert(digitCount(42) == digitCount(-42) == 2)
    assert(digitCount(121) == digitCount(-121) == 3)
    print("Passed. (Add more tests to be more sure!)")

def testKthDigit():
    print("Testing kthDigit()...", end="")
    assert(kthDigit(789, 0) == kthDigit(-789, 0) == 9)
    assert(kthDigit(789, 1) == kthDigit(-789, 1) == 8)
    assert(kthDigit(789, 2) == kthDigit(-789, 2) == 7)
    assert(kthDigit(789, 3) == kthDigit(-789, 3) == 0)
    assert(kthDigit(789, 4) == kthDigit(-789, 4) == 0)
    print("Passed. (Add more tests to be more sure!)")

def testReplaceKthDigit():
    print("Testing replaceKthDigit()...", end="")
    assert(replaceKthDigit(789, 0, 6) == 786)
    assert(replaceKthDigit(789, 1, 6) == 769)
    assert(replaceKthDigit(789, 2, 6) == 689)
    assert(replaceKthDigit(789, 3, 6) == 6789)
    assert(replaceKthDigit(789, 4, 6) == 60789)
    print("Passed. (Add more tests to be more sure!)")

def testGetLeftmostDigit():
    print("Testing getLeftmostDigit()...", end="")
    assert(getLeftmostDigit(7089) == 7)
    assert(getLeftmostDigit(89) == 8)
    assert(getLeftmostDigit(9) == 9)
    assert(getLeftmostDigit(0) == 0)
    print("Passed. (Add more tests to be more sure!)")

def testClearLeftmostDigit():
    print("Testing clearLeftmostDigit()...", end="")
    assert(clearLeftmostDigit(789) == 89)
    assert(clearLeftmostDigit(89) == 9)
    assert(clearLeftmostDigit(9) == 0)
    assert(clearLeftmostDigit(0) == 0)
    assert(clearLeftmostDigit(60789) == 789)
    print("Passed. (Add more tests to be more sure!)")

def testMakeMove():
    print("Testing makeMove()...", end="")
    assert(makeMove(8, 1, 1) == 1)
    assert(makeMove(888888, 1, 1) == 188888)
    assert(makeMove(888888, 2, 1) == 818888)
    assert(makeMove(888888, 5, 2) == 888828)
    assert(makeMove(888888, 6, 2) == 888882)
    assert(makeMove(888888, 6, 3) == "move must be 1 or 2!")
    assert(makeMove(888888, 7, 1) == "offboard!")
    assert(makeMove(888881, 6, 1) == "occupied!")
    print("Passed. (Add more tests to be more sure!)")    

def testIsWin():
    print("Testing isWin()...", end="")
    assert(isWin(888888) == False)
    assert(isWin(112888) == True)
    assert(isWin(811288) == True)
    assert(isWin(888112) == True)
    assert(isWin(211222) == True)
    assert(isWin(212212) == False)
    print("Passed. (Add more tests to be more sure!)")

def testIsFull():
    print("Testing isFull()...", end="")
    assert(isFull(888888) == False)
    assert(isFull(121888) == False)
    assert(isFull(812188) == False)
    assert(isFull(888121) == False)
    assert(isFull(212122) == True)
    assert(isFull(212212) == True)
    print("Passed. (Add more tests to be more sure!)")

def testPlay112():
    print ("Testing play112()...",end=" ")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print ("Passed!")

def testAll():
    testSumOfSquaresOfDigits()
    testIsHappyNumber()
    testNthHappyNumber()
    testNthCarolPrime()
    testCarrylessMultiply()
    testMakeBoard()
    testDigitCount()
    testKthDigit()
    testReplaceKthDigit()
    testGetLeftmostDigit()
    testClearLeftmostDigit()
    testMakeMove()
    testIsWin()
    testIsFull()
    testPlay112()

if __name__ == "__main__":
    testAll()
