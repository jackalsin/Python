def removeRowAndCol(A, row, col):
    (rows,cols)=(len(A),len(A[0]))
    aRemove=[]
    for currentRow in range (rows):
        if currentRow!=row:
            aRemove+=[A[currentRow][:col]+A[currentRow][col+1:]]
    # print(aRemove)
    return aRemove


def testRemoveRowAndCol():
    print("Testing removeRowAndCol()...", end="")
    a = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]]
    assert(removeRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]])
    assert(removeRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]])
    print("Passed!")

testRemoveRowAndCol()


def destructiveRemoveRowAndCol(A, row, col):
    (rows,cols)=(len(A),len(A[0]))
    A.remove(A[row])
    for currentRow in range(len(A)):
        A[currentRow].remove(A[currentRow][col])
    print(A)
            

def testDestructiveRemoveRowAndCol():
    print("Testing removeRowAndCol()...", end="")
    a = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]]
    assert(destructiveRemoveRowAndCol(a, 1, 2) == None)
    assert(a == [[2, 3, 5], [0, 1, 3]])
    a = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]]
    assert(destructiveRemoveRowAndCol(a, 0, 0) == None)
    assert(a == [[7, 6, 5], [1, 2, 3]])
    print("Passed!")

testDestructiveRemoveRowAndCol()

def getAvg(a,currentCol):
    (rows,cols)=(len(a),len(a[0]))
    sum=0
    count=0
    for row in range (rows):
        if a[row][currentCol]!=-1:
            sum+=a[row][currentCol]
            count+=1 
    if count==0:
        return None
    else:
        return sum/count

def bestQuiz(a):
    currentCol=None
    bestCol=None
    currentAvg=None
    bestAvg=0
    (rows,cols)=(len(a),len(a[0]))
    count=0
    for currentCol in range (cols):
        currentAvg=getAvg(a,currentCol)
        if currentAvg!=None and currentAvg>bestAvg:
            bestCol=currentCol
            bestAvg=currentAvg    
        count+=1
    # print(bestCol)
    return bestCol if count!=0 else None # place your answer here!

def testBestQuiz():
    print("Testing bestQuiz()...", end="")
    a = [ [ 88,  80, 91 ],
        [ 68, 100, -1 ]]
    assert(bestQuiz(a) == 2)
    a = [ [ 88,  80, 80 ],
            [ 68, 100, 100 ]]
    assert(bestQuiz(a) == 1)
    a = [ [88,  -1, -1 ],
        [68, -1, -1 ]]
    assert(bestQuiz(a) == 0)
    a = [ [-1,  -1, -1 ],
        [-1, -1, -1 ]]
    assert(bestQuiz(a) == None)
    print("Passed!")

testBestQuiz()


def wordSearch(board, word):
    (rows,cols)=(len(board),len(board[0]))
    for row in range(rows):
        for col in range (cols):
            result=wordSearchInCell(board,word,row,col)
            if result==True:
                return True

    return False # place your answer here!

def wordSearchInCell(board,word,row,col):
    for dir in range(8):
        result=wordSearchInCellInDirection(board,word,row,col,dir)
        if result==True:
            return True
    return False

def wordSearchInCellInDirection(board,word,startRow,startCol,dir):
    (rows,cols)=(len(board),len(board[0]))
    direction = [(-1,1),(0,1),(1,1),
                (-1,0),     (1,0),
                (-1,-1),(0,-1),(1,-1)
                ]

    (drow,dcol)=(direction[dir])
    wordIndex=0;
    deltaI=0
    while (wordIndex<len(word)):
        row=startRow+deltaI*drow
        col=startCol+deltaI*dcol
        if ((row<0 or row>=rows) or (col<0 or col>=cols)):
            return False
        elif (not (type(board[row][col])==int)):
            if board[row][col]!=word[wordIndex]:
                return False
            wordIndex+=1
            deltaI+=1
        else:
            wordIndex+=board[row][col]
            deltaI+=1
            if (len(word)<board[row][col]):
                return False
    return True

def testWordSearch():
    print("Testing wordSearch()...", end="")
    board = [ [ 'p', 'i', 'g' ],
              [ 's',   2, 'c' ]
            ]
    assert(wordSearch(board, "cow") == True)
    assert(wordSearch(board, "cows") == True)
    assert(wordSearch(board, "coat") == False)
    assert(wordSearch(board, "pig") == True)
    assert(wordSearch(board, "z") == False)
    assert(wordSearch(board, "zz") == True)
    print("Passed!")

testWordSearch() # with integer wildcards!
