# word seach
def wordSearch(board,word):
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            result=wordSearchFromCell(board, row, col, word)
            if result!=None:
                return result 

    return None

def wordSearchFromCell(board,startRow,startCol,word):
    (rows, cols) = (len(board),len(board[0]))
    
    for direction in range (8):
        result=wordSearchFromCellInDirection(board,startRow,startCol,
                                                        word,direction)
        if result!=None:
            return result 
    return None

def wordSearchFromCellInDirection(board,startRow,startCol,word,direction):
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    drow,dcol = dirs[direction]
    (rows, cols) = (len(board),len(board[0]))
    for i in range(len(word)):
        row=startRow+i*drow
        col=startCol+i*dcol
        if ((row<0 or row>=rows) or (col<0 or col>=cols) or (word[i] != board[row][col])):
            return None
    return (word, startRow,startCol,dirs[direction])

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