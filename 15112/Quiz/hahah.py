def nQueens(n):
    print("enter nQueens")
    queenRow = [-1] * n 
    def isValid(row,col):
        print("n = ", n)
        for qcol in range(n):
            qrow = queenRow[qcol]
            if((qrow == row) or (qcol == col) or ((qrow + qcol) == (row + col)) or
                 ((qcol - qrow) == (col - row))):
                print('return False')
                    return False
        return True
        
    def display(queenRow):
        print("enter display")
        print(queenRow)
        return
    def solve(col):
        nonlocal queenRow
        if (n == col):
            return display(queenRow)
        else:
            for row in range(n):
                queenRow[col] = row
                print("row = %d and col = %d " % (row,col))
                if isValid(row,col):
                    print("isValid")
                    result = solve(col + 1)
                    if result != None:
                        return result
                    queenRow[col] = -1
            return None 
    return solve(0)

nQueens(4)

















nQueens(4)
