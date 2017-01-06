#Homework 5!!!! Name: Zhiwei Xin Andrew ID: zxin
import copy

def isMagicSquare(a):
    if (isEmpty(a) or ((not (isRag(a))) and (len(a)!=len(a[0]))) 
        or (noDuplicateElem(a)==False)): 
        # print("because of isEmpty") # for test only
        return False
    else:
        (rows,cols)=(len(a),len(a[0]))
        exampleSum=sumOfList(getCol(a,0))
        for col in range(1,cols):
            if sumOfList(getCol(a,col))!=exampleSum:
                # print("because of Col",getCol(a,col),"col is ",col) # for test only
                return False
        for row in range(rows):
            if sumOfList(a[row])!=exampleSum:
                # print("because of row") # for test only
                return False
        for diagonal in range (2):
            if sumOfList(getDiagonal(a)[diagonal])!=exampleSum:
                # print("because of diag") # for test only
                return False
        return True

def getDiagonal(a): # return[[main diag],[sec diag]]
    (rows,cols)=(len(a),len(a[0]))
    diagonalList=[[],[]]
    for row in range(rows):
        diagonalList[0].append(a[row][row])
    for row in range(rows):
        diagonalList[1].append(a[row][rows-1-row])
    return diagonalList

def getCol(a,col):
    (rows,cols)=(len(a),len(a[0]))
    colList=[]
    for row in range(rows):
        colList.append(a[row][col])
    # print(colList)
    return colList

def isRag(a): # return true when is not ragged
    (rows,cols)=(len(a),len(a[0]))
    for row in range(rows-1): # to test if cols are equal
        if len(a[row])!=len(a[row+1]):
            return False
    for col in range(cols-1):
        if len(getCol(a,col))!=len(getCol(a,col+1)):
            return False
    return True

def sumOfList(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    return sum

def isEmpty(a):
    if a==[]:
        return True
    else:
        return False

################ Question 2 ###########
def isKingTour(board):
    (rows,cols)=(len(board),len(board[0]))
    if not isValidKingBoard(board):
        return False
    else:
        for currentNumber in range(1,rows*cols):
            (startRow,startCol)=elemExist(board,currentNumber) # get Position
            result=currentPositionOk(board,startRow,startCol)
            if result==False:
                return result
        return True
        
# check n in range (1, n*n+1) and appear only once and cols=rows
def elemExist(board,elem): # return row and col when true, return False
    (rows,cols)=(len(board),len(board[0]))
    (row,col)=(0,0)
    while (row<rows):
        col=0
        while(col<cols):
            if board[row][col]==elem:
                return (row,col)
            col+=1
        row+=1
    return False

def noDuplicateElem(board):
    (rows,cols)=(len(board),len(board[0]))
    boardCopy=copy.deepcopy(board)
    oneDboard=[]
    for row in range (rows):
        for col in range (cols):
            oneDboard.append(board[row][col])
    for index in range(len(oneDboard)):
        if oneDboard.count(oneDboard[index])>1:
            return False
    return True

def isValidKingBoard(board): # alll
    boardCopy=copy.deepcopy(board)
    (rows,cols)=(len(board),len(board[0]))
    if cols!=rows or (noDuplicateElem(board)==False): # isRag
        return False
    else:
        for i in range(1,cols*rows+1):
            if not (elemExist(boardCopy,i)==False):
                continue
            # print("when i=%d return False" % (i)) # for test only
            return False
        return True
       
def currentPositionOk(board,startRow,startCol):
    (rows,cols)=(len(board),len(board[0]))
    direction=[(-1,1),(0,1),(1,1),
                (-1,0),     (1,0),
                (-1,-1),(0,-1),(1,-1)]
    tgtNum=board[startRow][startCol]+1
    for dir in range(len(direction)):
        (drow,dcol)=direction[dir]
        (nextRow,nextCol)=(startRow+drow,startCol+dcol)
        if ((nextRow<0 or nextRow>=rows) or (nextCol<0 or nextCol>=cols)):
            continue
        elif board[nextRow][nextCol]==tgtNum:
            return True
    return False 

def isLegalSudoku(board):
    if not isSquare(board):
        return False
    else:
        return 42

def noDuplicateValueIn1dList(list):
    for index in range(len(list)):
        if list.count(list[index])>1:
            return False
    return True

def returnListWithoutZero(list):
    noZeroValues=[]
    for index in range(len(list)):
        if list[index]!=0:
            noZeroValues.append(list[index])
    return noZeroValues
############### Question 3 ############
def areLegalValues(values): # value is a 1d list
    noZeroValues=returnListWithoutZero(values)
    # print(noZeroValues) # for test only
    for index in range(len(values)):
        if type(values[index])!=int:
            return False
        elif values[index]<0 or values[index]> len(values):
            return False
        elif not noDuplicateValueIn1dList(noZeroValues):
            return False
    return True

def isLegalRow(board, row):
    return areLegalValues(board[row])

def isLegalCol(board, col):
    colList=getCol(board,col)
    return areLegalValues(colList)

def isLegalBlock(board, block):
    N=round((len(board))*0.5)
    blockIn1dList=getBlockIn1dList(board,block)
    return areLegalValues(blockIn1dList)

def getBlockIn1dList(board,block):
    N=round((len(board))**0.5)
    startRow=block//N*N
    startCol=block%N*N
    blockIn1dList=[]
    # print("startRow,startCol,N",startRow,startCol,N)
    for row in range (startRow,startRow+N):
        for col in range(startCol,startCol+N):
            blockIn1dList.append(board[row][col])
    # print(blockIn1dList) # for test only
    return blockIn1dList

def isSquare(board):
    if (len(board)==0) or (len(board[0])==0): # empty row
        return False
    rows=len(board)
    for row in range(rows): # check cols in demension
        if len(board[row]) != len(board[0]):
            return False
    cols=len(board[0])
    standardColLen=getCol(board,0)
    for col in range(1,cols):
        currentColList=getCol(board,col)
        if len(currentColList) != len(standardColLen):
            return False
    if cols!=rows:
        return False
    return True


def isLegalSudoku(board):
    if not isSquare(board):
        return False
    (rows,cols)=(len(board),len(board[0]))
    for row in range (rows): #since cols=rows, check at the same time
        if isLegalRow(board,row) == False or isLegalCol(board,row) == False:
            return False
    N=round((len(board))**0.5)
    for n in range(N*N):
        if isLegalBlock(board,n)==False:
            return False
    return True



############### Question 4 ################
def wordSearch(board, word): # cited from Notes
    print(board)
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            result = wordSearchFromCell(board, word, row, col)
            if (result != None):
                return result
    return None

def wordSearchFromCell(board, word, startRow, startCol): # cited from Notes
    for drow in [-1, 0, +1]:
        for dcol in [-1, 0, +1]:
            if ((drow != 0) or (dcol != 0)):
                result = wordSearchFromCellInDirection(board, word,
                                                       startRow, startCol,
                                                       drow, dcol)
                if (result != None):
                    return result
    return None

def wordSearchFromCellInDirection(board, word, startRow, startCol, drow, dcol):
    (rows, cols) = (len(board), len(board[0]))
    dirNames = [ ["up-left"  ,   "up", "up-right"],
                 ["left"     ,   ""  , "right"   ],
                 ["down-left", "down", "down-right" ] ]
    for i in range(len(word)):
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or
            (col < 0) or (col >= cols) or
            (board[row][col] != word[i])):
            return None
    return (word, (startRow, startCol), dirNames[drow+1][dcol+1])


def makeWordSearch(wordList, replaceEmpties) :
    board=[]
    if wordList==[]:
        return None
    wordIndex=0 
    while(wordIndex<len(wordList)):
        if board!=[] and wordSearch(board,wordList[wordIndex])!=None:
            wordIndex+=1
            continue
        if len(wordList[wordIndex])>len(board):
            addWordInNewLine(board,wordList[wordIndex])
        elif not (searchLowestCostPosition(board,wordList[wordIndex]) == None):
            (startRow,startCol,direction,cost)=searchLowestCostPosition(board,
                wordList[wordIndex])
            addWordByReplace(board,wordList[wordIndex],startRow,startCol,
                direction)
        else:
            addWordInNewLine(board,wordList[wordIndex])
        wordIndex+=1

    displayBoard(board,replaceEmpties)
    return board

def addWordInNewLine(board,word):
    newLine=[]
    for letter in word:
        newLine.append(letter)
    board.append(newLine)
    rows=len(board)
    for row in range(rows): # do cols but last one
        while(len(board[row])<rows):
            board[row].append('-')
    cols=len(board[0])
    while(len(board)<cols): # do rows
        board.append(['-']*cols)
    while(len(board[rows-1])<cols):
        board[rows-1].append('-')
    print("Now we are add ",word,'\n here is the board',board)
# board=[]
# addWordInNewLine(board,'kiss')
# print(board)


# return None when no position or return 
# (startRow,startCol,direction)
def searchLowestCostPosition(board,word): 
    (rows,cols)=(len(board),len(board[0]))
    lowestCost=len(word);result=None
    for row in range(rows):
        for col in range (cols):
            for dir in range(8):
                current=searchLowestCostPositionInDirection(board,
                    word,row,col,dir)
                # print("not in direction",row,col,dir,"\n",current)
                if current!=None:
                    if current[3]<lowestCost:
                        result=current
                        lowestCost=current[3]
                    elif current[3]==lowestCost and result==None:
                        result=current
    if result!=None:
        return result #
    else:# man d eshihou
        return None

def searchLowestCostPositionInDirection(board,word,startRow,startCol,direction):
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[direction]    
    cost=0
    for i in range(len(word)):
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols)):
            return None
        else:
            if (board[row][col] == word[i]): # 在这里补充条件 word Replace 改
                continue
            elif (board[row][col] == '-'):
                # print("now i= %d and row col=%d %d" %(i,row,col))
                cost+=1
            else:
                return None
    return [startRow,startCol,dirs[direction],cost]

def addWordByReplace(board,word,startRow,startCol,direction):
    (rows, cols) = (len(board), len(board[0]))
    (drow,dcol) = (direction[0],direction[1])    
    for i in range(len(word)):
        row = startRow + i*drow
        col = startCol + i*dcol
        board[row][col]=word[i]

def displayBoard(board,replaceEmpties):
    if replaceEmpties==True:
        (rows,cols)=(len(board),len(board[0]))
        for row in range(rows):
            for col in range(cols):
                if board[row][col]=='-':
                    replaceDash(board,row,col)

def replaceDash(board,startRow,startCol):
    alphabet=[chr(ord('a')+i) for i in range(26)]
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (rows, cols) = (len(board), len(board[0]))
    for dir in range(8):
        (drow,dcol) = (dirs[dir][0],dirs[dir][1])
        row = startRow + drow
        col = startCol + dcol
        if ((row >= 0) and (row < rows) and
            (col >= 0) and (col < cols) and
            (board[row][col] == alphabet[0])):
            alphabet.remove(alphabet[0])
    board[startRow][startCol]=alphabet[0]

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################
def testIsRag():
    print("Testing isRag()...", end="")
    assert(isRag([[1,2,3],[1,2,3],[1,2,3]]) == True)
    assert(isRag([[1,2,3],[1,3],[1,2,3]]) == False)
    assert(isRag([[1,2,3],[1,2,3]]) == True)
    print("Passed. (Add more tests to be more sure!)")

def testIsMagicSquare():
    print("Testing isMagicSquare()...", end="")
    A=[ [2,7,6],
        [9,5,1],
        [4,3,8]
      ]
    B=[ [2,7,6],
        [9,11,1],
        [4,3,8]
      ]    
    C=[ [2,7,6],
        [9,5,1],
        [4,3,11]
      ]
    D=[]
    E=[[1],[2],[3]]
    assert(isMagicSquare(A) == True)
    assert(isMagicSquare(B) == False)
    assert(isMagicSquare(C) == False)
    assert(isMagicSquare(D) == False)
    assert(isMagicSquare(E) == False)
    print("Passed. (Add more tests to be more sure!)")

def testIsEmpty():
    print("Testing isEmpty()...", end="")
    assert(isEmpty([[1,2,3],[1,2,3],[1,2,3]]) == False)
    assert(isEmpty([[1,2,3],[1,3],[1,2,3]]) == False)
    assert(isEmpty([]) == True)
    print("Passed. (Add more tests to be more sure!)")

def testGetCol():
    print("Testing getCol()...", end="")
    assert(getCol([[1,2,3],[1,2,3],[1,2,3]],1) == [2,2,2])
    assert(getCol([[1,2,3],[1,3,2],[1,2,3]],0) == [1,1,1])
    assert(getCol([[1,2,3],[1,3,2],[1,2,3]],2) == [3,2,3])
    print("Passed. (Add more tests to be more sure!)")

def testGetDiagonal():
    print("Testing getDiagonal()...", end="")
    assert(getDiagonal([[1,2,3],[1,2,3],[1,2,3]]) == [[1,2,3],[3,2,1]])
    assert(getDiagonal([[1,2,3],[1,3,2],[1,2,3]]) == [[1,3,3],[3,3,1]])
    assert(getDiagonal([[7,3,5],[2,3,2],[1,2,3]]) == [[7,3,3],[5,3,1]])
    print("Passed. (Add more tests to be more sure!)")

def testElemExist():
    print("Testing elemExist()...", end="")
    A1=[[1,2,3],[4,5,6],[7,8,9]]
    A2=[[1,2,2],[4,5,6],[7,8,9]]
    A3=[[2,3],[4,5,6],[7,8,9]]
    A4=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    assert(elemExist(A1,1) == (0,0))
    assert(elemExist(A1,4) == (1,0))
    assert(elemExist(A4,9) == (2,0))
    print("Passed. (Add more tests to be more sure!)")

def testNoDuplicateElem():
    print("Testing noDuplicateElem()...", end="")
    A1=[[1,2,3],[4,5,6],[7,8,9]]
    A2=[[1,2,2],[4,5,6],[7,8,9]]
    A3=[[2,3],[4,5,6],[7,8,9]]
    A4=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    assert(noDuplicateElem(A1) == True)
    assert(noDuplicateElem(A2) == False)
    assert(noDuplicateElem(A4) == True)
    print("Passed. (Add more tests to be more sure!)")

def testIsValidKingBoard():
    print("Testing isValidKingBoard()...", end="")
    A1=[[1,2,3],[4,5,6],[7,8,9]]
    A2=[[1,2,2],[4,5,6],[7,8,9]]
    A3=[[2,3],[4,5,6],[7,8,9]]
    A4=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    assert(isValidKingBoard(A1) == True)
    assert(isValidKingBoard(A2) == False)
    assert(isValidKingBoard(A3) == False)
    assert(isValidKingBoard(A4) == True)
    print("Passed. (Add more tests to be more sure!)")

def testCurrentPositionOk():
    print("Testing currentPositionOk()...", end="")
    A1=[[1,2,3],[4,5,6],[7,8,9]]
    A4=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    assert(currentPositionOk(A1,0,1) == True)
    assert(currentPositionOk(A1,0,2) == False)
    assert(currentPositionOk(A4,2,3) == False)
    assert(currentPositionOk(A4,2,2) == True)
    print("Passed. (Add more tests to be more sure!)")

def testIsKingTour():
    print("Testing isKingTour()...", end="")
    A1= [   [  3, 2, 1 ],
            [  6, 4, 9 ],  
            [  5, 7, 8 ] ]
    A2=[[  1, 2, 3 ],
        [  7, 4, 8 ],
        [  6, 5, 9 ] ]
    A3=[[ 3, 2, 1 ],
        [ 6, 4, 0 ],
        [ 5, 7, 8 ]]
    A4=[[  1, 14, 15, 16],
        [ 13,  2,  7,  6],
        [ 12,  8,  3,  5],
        [ 11, 10,  9,  4]]
    assert(isKingTour(A1) == True)
    assert(isKingTour(A2) == False)
    assert(isKingTour(A3) == False)
    assert(isKingTour(A4) == True)
    print("Passed. (Add more tests to be more sure!)")

def testAreLegalValues():
    print("Testing areLegalValues()...", end="")
    assert(areLegalValues([ 5, 3, 0, 0, 7, 0, 0, 0, 0 ]) == True)
    assert(areLegalValues([ 5, 3, 9, 0, 7, 0, 0, 0, 0 ]) == True)
    assert(areLegalValues([ 5, 3, 3, 0, 7, 0, 0, 0, 0 ]) == False)
    assert(areLegalValues([ 5, 3, 10, 0, 7, 0, 0, 0, 0 ]) == False)
    print("Passed. (Add more tests to be more sure!)")

def testIsLegalRow():
    A=[
      [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
      [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
      [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
      [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
      [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
      [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
      [ 0, 6, 0, 6, 0, 0, 2, 8, 0 ],
      [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
      [ 0, 0, 10, 0, 8, 0, 0, 7, 9 ]
    ]
    print("Testing isLegalRow()...", end="")
    assert(isLegalRow(A,1) == True)
    assert(isLegalRow(A,2) == True)
    assert(isLegalRow(A,6) == False)
    assert(isLegalRow(A,8) == False)
    print("Passed. (Add more tests to be more sure!)")

def testIsLegalCol():
    A=[
      [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
      [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
      [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
      [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
      [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
      [ 7, 0, 0, 0, 2, 0, 2, 0, 6 ],
      [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
      [ 0, 0, 0, 4, 1, 9, 0, 0, 10 ],
      [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    print("Testing isLegalCol()...", end="")
    assert(isLegalCol(A,1) == True)
    assert(isLegalCol(A,2) == True)
    assert(isLegalCol(A,6) == False)
    assert(isLegalCol(A,8) == False)
    print("Passed. (Add more tests to be more sure!)")

def testIsLegalBlock():
    print("Testing isLegalBlock()...", end="")
    assert(isLegalBlock(A,1) == True)
    assert(isLegalBlock(A,2) == True)
    assert(isLegalBlock(A,6) == False)
    assert(isLegalBlock(A,8) == False)
    print("Passed. (Add more tests to be more sure!)")

def testGetBlockIn1dList():
    A=[
      [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
      [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
      [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
      [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
      [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
      [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
      [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
      [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
      [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    print("Testing getBlockIn1dList()...", end="")
    assert(getBlockIn1dList(A,0) == [5,3,0,6,0,0,0,9,8])
    assert(getBlockIn1dList(A,2) == [0,0,0,0,0,0,0,6,0])
    assert(getBlockIn1dList(A,6) == [0,6,0,0,0,0,0,0,0])
    assert(getBlockIn1dList(A,8) == [2,8,0,0,0,5,0,7,9])
    print("Passed. (Add more tests to be more sure!)")

def testIsSquare():
    print("Testing isSquare()...", end="")
    assert(isSquare([]) == False)
    assert(isSquare([[1,2,3],[1,2,3],[1,2,3]]) == True)
    assert(isSquare([[1,2],[1,2,3],[1,2,3]]) == False)
    assert(isSquare([[1,2,3],[1,2,3]]) == False)
    print("Passed. (Add more tests to be more sure!)")

def testIsLegalSudoku():
    A=[
      [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
      [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
      [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
      [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
      [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
      [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
      [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
      [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
      [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    A1=[
      [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
      [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
      [ 6, 9, 8, 0, 0, 0, 0, 6, 0 ],
      [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
      [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
      [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
      [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
      [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
      [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    A2=[]
    A3=[[],[1,2,3],[1,2,3]]
    A4=[
      [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
      [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
      [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
      [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
      [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
      [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
      [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
      [ 10, 0, 0, 4, 1, 9, 0, 0, 5 ],
      [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    print("Testing isLegalSudoku()...", end="")
    assert(isLegalSudoku(A) == True)
    assert(isLegalSudoku(A1) == False)
    assert(isLegalSudoku(A2) == False)
    assert(isLegalSudoku(A3) == False)
    assert(isLegalSudoku(A4) == False)
    print("Passed. (Add more tests to be more sure!)")

def testMakeWordSearch():
    print("Testing makeWordSearch()...", end="")
    board = makeWordSearch([], False)
    assert(board == None)

    board = makeWordSearch(["ab"], False)
    assert(board == [['a', 'b'], ['-', '-'] ])
    
    board = makeWordSearch(["ab"], True)
    # print(board)
    assert(board == [['a', 'b'], ['c', 'd'] ])
    assert(board == [['a', 'b'], ['c', 'd']])
    # print("we passed True")

    board = makeWordSearch(["ab", "bc", "cd"], False)
    # print("we are testing ab bc cd")
    # print(board)
    # assert(board == [['a', 'b'], ['c', 'd'] ])
    # print("we passed ab bc cd")
    # board = makeWordSearch(["ab", "bc", "cd", "de"], False)
    # print("board is here",board)
    # assert(board == [['a', 'b', '-'], ['c', 'd', '-'], ['d', 'e', '-']])
    # board = makeWordSearch(["ab", "bc", "cd", "de"], True)
    # assert(board == [['a', 'b', 'a'], ['c', 'd', 'c'], ['d', 'e', 'a']])

    # board = makeWordSearch(["abc"], False)
    # assert(board == [['a', 'b', 'c'], ['-', '-', '-'], ['-', '-', '-']])
    # board = makeWordSearch(["abc"], True)
    # assert(board == [['a', 'b', 'c'], ['c', 'd', 'a'], ['a', 'b', 'c']])

    # board = makeWordSearch(["abc", "adc", "bd", "bef", "gfc"], False)
    # assert(board == [['a', 'b', 'c'], ['d', 'e', '-'], ['c', 'f', 'g']])
    # board = makeWordSearch(["abc", "adc", "bd", "bef", "gfc"], True)
    # assert(board == [['a', 'b', 'c'], ['d', 'e', 'a'], ['c', 'f', 'g']])

    print("Passed!")

def testAddWordInNewLine():
    print("Testing addWordInNewLine()...", end="")
    board = []
    addWordInNewLine(board, 'kiss')
    assert(board == [   ['k', 'i', 's', 's'], 
                        ['-', '-', '-', '-'], 
                        ['-', '-', '-', '-'], 
                        ['-', '-', '-', '-']])
    board=[ ['k', 'i', 's'], 
            ['k', 'i', 's'], 
            ['k', 'i', 's'] 
            ]
    addWordInNewLine(board, 'love')
    assert(board == [   ['k', 'i', 's', '-'], 
                        ['k', 'i', 's', '-'], 
                        ['k', 'i', 's', '-'], 
                        ['l', 'o', 'v', 'e']])
    board=[ ['k', 'i', 's'], 
            ['k', 'i', 's'], 
            ['k', 'i', 's'] 
            ]
    addWordInNewLine(board, 'ok')
    assert(board == [   ['k', 'i', 's', '-'], 
                        ['k', 'i', 's', '-'], 
                        ['k', 'i', 's', '-'], 
                        ['o', 'k', '-', '-']])
    print("Passed!")

def testSearchLowestCostPosition():
    print("Testing searchLowestCostPosition()...", end="")
    board =[['k', 'i', 's', 's'], 
            ['-', '-', '-', '-'], 
            ['-', '-', '-', '-'], 
            ['-', '-', '-', '-']]
    # print(searchLowestCostPosition(board, 'love'))        
    assert(searchLowestCostPosition(board, 'love') == [1, 0, (0, 1),4])
    assert(searchLowestCostPosition(board, 'lovee') == None)   
    board =[['k', 'i', 's', 's'], 
            ['l', '-', '-', '-'], 
            ['-', '-', '-', '-'], 
            ['-', '-', '-', '-']]
    # print('result is here',searchLowestCostPosition(board, 'lo'))
    assert(searchLowestCostPosition(board, 'lo') == [1, 0, (0, 1),1])
    board =[['k', 't', 's', 's'], 
            ['k', 'i', '-', '-'], 
            ['-', '-', '-', '-'], 
            ['-', '-', '-', '-']]
    assert(searchLowestCostPosition(board,'kb')==[1, 0, (1, 0),1])
    assert(searchLowestCostPosition(board, 'icc') == [1, 1, (0, 1),2])
    print("Passed!")

def testAddWordByReplace():
    print("Testing addWordByReplace()...", end="")
    board =[['k', 'i', 's', 's'], 
            ['-', '-', '-', '-'], 
            ['-', '-', '-', '-'], 
            ['-', '-', '-', '-']]
    addWordByReplace(board, 'love',1,0,(0, 1))
    assert(board==[ ['k', 'i', 's', 's'], 
                    ['l', 'o', 'v', 'e'], 
                    ['-', '-', '-', '-'], 
                    ['-', '-', '-', '-']])
    
    board =[['k', 'i', 's', 's'], 
            ['k', '-', '-', '-'], 
            ['-', '-', '-', '-'], 
            ['-', '-', '-', '-']]
    addWordByReplace(board, 'klo',1,0, (0, 1))   
    print("addWordByReplace",board)     
    assert(board==[ ['k', 'i', 's', 's'], 
                    ['k', 'l', 'o', '-'], 
                    ['-', '-', '-', '-'], 
                    ['-', '-', '-', '-']])

    board=[ ['k', 'i', 's', 's'], 
            ['k', 'i', '-', '-'], 
            ['-', '-', '-', '-'], 
            ['-', '-', '-', '-']]
    addWordByReplace(board,'lo',1, 2, (0, 1))
    assert(board==[ ['k', 'i', 's', 's'], 
                    ['k', 'i', 'l', 'o'], 
                    ['-', '-', '-', '-'], 
                    ['-', '-', '-', '-']])
    print("Passed!")

def testDisplayBoard():
    print("Testing displayBoard()...", end="")
    board =[['k', 'i', 's', 's'], 
            ['-', '-', '-', '-'], 
            ['-', '-', '-', '-'], 
            ['-', '-', '-', '-']]
    displayBoard(board, False)
    assert(board==[ ['k', 'i', 's', 's'], 
                    ['-', '-', '-', '-'], 
                    ['-', '-', '-', '-'], 
                    ['-', '-', '-', '-']])
    
    board =[['k', 'i', 's', 's'], 
            ['k', 'c', 'd', 'g'], 
            ['a', 'z', 'f', '-'], 
            ['t', 't', '-', '-']]
    displayBoard(board, True)
    print(board)        
    assert(board==[ ['k', 'i', 's', 's'], 
                    ['k', 'c', 'd', 'g'], 
                    ['a', 'z', 'f', 'a'], 
                    ['t', 't', 'b', 'c']])

    board=[ ['k', 'i', 's', 's'], 
            ['k', 'i', 'g', 'o'], 
            ['a', 'w', 'a', 'y'], 
            ['-', '-', '-', '-']]
    displayBoard(board,True)
    assert(board==[ ['k', 'i', 's', 's'], 
                    ['k', 'i', 'g', 'o'], 
                    ['a', 'w', 'a', 'y'], 
                    ['b', 'c', 'b', 'c']])
    print("Passed!")    

def testAllFunction():
    testIsEmpty()
    testIsRag()
    testGetCol()
    testGetDiagonal()
    testIsMagicSquare()

    testElemExist()
    testIsValidKingBoard()
    testNoDuplicateElem()
    testCurrentPositionOk()
    testIsKingTour()

    testAreLegalValues()
    testIsLegalCol()
    testIsLegalRow()
    testGetBlockIn1dList()
    testIsSquare()
    testIsLegalSudoku()

    # testMakeWordSearch()
    testAddWordInNewLine()
    testSearchLowestCostPosition()
    testAddWordByReplace()
    # testDisplayBoard()

testAllFunction()