def wordSearch(board,word):
    (rows,cols)=(len(board),len(board[0]))
    result=None
    for row in range (rows):
        for col in range (cols):
            result=wordSearchInCell(board,word,row,col)
            if result!=None:
                return result
    return result

def wordSearchInCell(board,word,startRow,startCol):
    result=None
    for direction in range (8):
        result=wordSearchInCellInDirection(board,word,startRow,startCol,direction)
        if result!=None:
            return result
    return result

def wordSearchInCellInDirection(board,word,startRow,startCol,dir):
    result=None
    (rows, cols) = (len(board), len(board[0]))
    direction=[(-1,1),(0,1),(1,1),
                (-1,0),     (1,0),
                (-1,-1),(0,-1),(1,-1)]
    directionName=[ "up-left"  ,   "up", "up-right",
                 "left"     ,         "right",
                 "down-left", "down", "down-right" ]
    (dirRow,dirCol)=direction[dir]
    for i in range (len(word)):
        currentRow=startRow+dirRow*i
        currentCol=startCol+dirCol*i
        # print("Now we are testing ", currentRow,currentCol)
        if ((currentCol<0 or currentRow>=rows) or 
            (currentCol<0 or currentCol>=cols) or 
            (board[currentRow][currentCol]!=word[i])):
            return None
    print((word,direction[dir],directionName[dir]))
    return (word,direction[dir],directionName[dir])

def testWordSearch():
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'o', 'a', 't' ],
              [ 'u', 'r', 'k' ],
            ]
    print(wordSearch(board, "dog")) # ('dog', (0, 0), 'right')
    print(wordSearch(board, "cat")) # ('cat', (1, 2), 'left')
    print(wordSearch(board, "tad")) # ('tad', (2, 2), 'up-left')
    print(wordSearch(board, "cow")) # None
testWordSearch()