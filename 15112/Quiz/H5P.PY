import copy
def isLatinSquare(a):
    (rows,cols)=(len(a),len(a[0]))
    aa=copy.copy(a)
    if rows * cols==0:
        return False
    for i in range(cols):
        target=a[0][i:]+a[0][:i]
        if target in aa:
            aa.remove(target)
        else:
            return False
    return True


def testIsLatinSquare():
    print("Testing isLatinSquare()...", end="")
    assert(isLatinSquare([['A','B','C'],['B','A','C'],['C','A','B']]) == False)
    assert(isLatinSquare([['A','B','C'],['B','C','A'],['C','A','B']]) == True)
    assert(isLatinSquare([['B','C','A'],['A','B','C'],['C','A','B']]) == True)

    assert(isLatinSquare([[],[],[]]) == False)
    print("Passed. (Add more tests to be more sure!)")
testIsLatinSquare()


# Write the function matrixAdd(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices, in the linear algebra sense) 
# and returns a new 2d list that is the result of  adding the two matrices.  
# Return None if the two matrices cannot be added for any reason.
def matrixAdd(m1,m2):
    (rows1,cols1)=(len(m1),len(m1[0]))
    (rows2,cols2)=(len(m2),len(m2[0]))
    if (rows1!=rows2) or (cols1!=cols2) or (rows1*cols1*cols2*rows2==0):
        return False
    sum=[[0]*cols1 for row in range(rows1)]
    for row in range (rows1):
        for col in range(cols1):
            sum[row][col]=m1[row][col]+m2[row][col]
    return sum

def testMatriAdd():
    print("Testing matrixAdd()...", end="")
    A=[[1,2,3],[4,5,6],[7,8,9]]
    B=[[5,6,7],[8,4,3],[3,4,6]]
    C=[[3,5],[3,4]]
    D=[[],[]]
    assert(matrixAdd(A,B) == [[6,8,10],[12,9,9],[10,12,15]])
    assert(matrixAdd(A,C) == False)
    assert(matrixAdd(D,D) == False)
    print("Passed. (Add more tests to be more sure!)")
testMatriAdd()

def matrixMultiply(m1,m2):
    (rows1,cols1)=(len(m1),len(m1[0]))
    (rows2,cols2)=(len(m2),len(m2[0]))
    if (rows1!=cols2) or (rows1*cols1*cols2*rows2==0):
        return False
    else:
        rows=rows1
        cols=cols2
    sum=[[0]*cols for row in range (rows)]
    for row in range(rows):
        for col in range(cols):
            sum[row][col]=getSum(m1,m2,row,col)
    print(sum)
    return sum

def getSum(m1,m2,row,col):
    (rows1,cols1)=(len(m1),len(m1[0]))
    (rows2,cols2)=(len(m2),len(m2[0]))
    unit=0
    # for (iCol,iRow) in zip (cols1,rows2):
    #     unit+=m1[row][iCol]*m2[col][iRow]
    iRow=iCol=0
    while(iCol<cols1):
        unit+=m1[row][iCol]*m2[iRow][col]
        iRow+=1
        iCol+=1
    return unit

def testMatrixMultiply():
    print("Testing matrixMultiply()...", end="")
    A=[[1,2,3],[4,5,6],[7,8,9]]
    B=[[5,6,7],[8,4,3],[3,4,6]]
    C=[[3,5],[3,4]]
    D=[[],[]]
    assert(matrixMultiply(A,B) == [[30,26,31],[78,68,79],[126,110,127]])
    assert(matrixMultiply(A,C) == False)
    assert(matrixMultiply(D,D) == False)
    print("Passed. (Add more tests to be more sure!)")
testMatrixMultiply()

# Helper function for print2dList.
# This finds the maximum length of the string
# representation of any item in the 2d list
def maxItemLength(a):
    maxLen = 0
    rows = len(a)
    cols = len(a[0])
    for row in range(rows):
        for col in range(cols):
            maxLen = max(maxLen, len(str(a[row][col])))
    return maxLen

# Because Python prints 2d lists on one row,
# we might want to write our own function
# that prints 2d lists a bit nicer.
def print2dList(a):
    if (a == []):
        # So we don't crash accessing a[0]
        print([])
        return
    rows = len(a)
    cols = len(a[0])
    fieldWidth = maxItemLength(a)
    print("[ ", end="")
    for row in range(rows):
        if (row > 0): print("\n  ", end="")
        print("[ ", end="")
        for col in range(cols):
            if (col > 0): print(", ", end="")
            # The next 2 lines print a[row][col] with the given fieldWidth
            formatSpec = "%" + str(fieldWidth) + "s"
            print(formatSpec % str(a[row][col]), end="")
        print(" ]", end="")
    print("]")


def playMemoryGame(rows, cols):
    board=makeABoard(rows,cols)
    displayBoard=[['-']*cols for row in range (rows)]
    (score1,score2)=(0,0)
    count=0
    player=0
    while(count<=rows*cols/2):
        player=player%2+1# so player 1 and player 2
        guessPosition=getGuessPosition(player,board,displayBoard)
        # example [(1,2),(3,4)]
        if (takeGuess(board,displayBoard,guessPosition)):
            count+=1
            if player==1:
                score1+=1
            else:
                socre2+=1
        player+=1
        print2dList(displayBoard)

def takeGuess(board,displayBoard,guessPosition):
    (rows,cols)=(len(board),len(board[0]))
    guess1Row=guessPosition[0][0]
    guess1Col=guessPosition[0][1]
    guess2Row=guessPosition[1][0]
    guess2Col=guessPosition[1][1]
    if (board[guess1Row][guess1Col]==board[guess2Row][guess2Col]):
        displayBoard[guess1Row][guess1Col]=board[guess1Row][guess1Col]
        displayBoard[guess2Row][guess2Col]=board[guess2Row][guess2Col]
        return True
    else:
        return False

def getGuessPosition(player,board,displayBoard):
    (rows,cols)=(len(board),len(board[0]))
    while True:
        response=input("Enter player %d's move ([[row1,col1],[row2,col2]]) --> "
                 % (player))
        inputResult=[]
        try:
            for item in response.split(' '):
                inputResult+=[item]
            print(inputResult)
            (row1,col1,row2,col2)=(int(inputResult[0])-1,int(inputResult[1])-1,
                int(inputResult[2])-1,int(inputResult[3])-1)
             # so that get the normal Value
            if ((col1<0 or row1<0 or col2 <0 or row2<0) 
                or (col1>cols or row1>rows or col2>cols or row2>rows)):
                print("Columns must be between 1 and %d\n Rows must be between 1 and %d " 
                    % (cols,rows), end="")
            elif(col1==col2 and row1==row2):
                print("You're entering the same position")
            elif (displayBoard[row1][col1]!='-') or (displayBoard[row2][col2]!='-'):
                print("That position has been occupied ", end="")
            else:
                print("we enter the return statement")
                return [[row1,col1],[row2,col2]]
        except:
            print("You must enter integer values! ", end="")
        print("Please try again.")

def makeABoard(rows,cols):
    result=[[0]*cols for row in range (rows)]
    count=0
    for row in range(rows):
        for col in range(cols):
            result[row][col]=round((count)%((rows*cols)/2))
            count+=1
    return result

cols=4
rows=4
# displayBoard=[['-']*cols for row in range (rows)]
# board=makeABoard(cols,rows)
# print(getGuessPosition(1,board,displayBoard))
playMemoryGame(rows, cols)