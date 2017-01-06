def nQueens(n):
    queenRow = [-1] * n
    def isLegal(row, col):
        # a position is legal if it's on the board (which we can assume
        # by way of our algorithm) and no prior queen (in a column < col)
        # attacks this position
        for qcol in range(col):
            qrow = queenRow[qcol]
            if ((qrow == row) or
                (qcol == col) or
                (qrow+qcol == row+col) or
                (qrow-qcol == row-col)):
                return False
        return True
    def make2dSolution(queenRow):
        solution = [(["- "] * n) for row in range(n)]
        for col in range(n):
            row = queenRow[col]
            solution[row][col] = "Q "
        return "\n".join(["".join(row) for row in solution])
    def solve(col):
        if (col == n):
            return make2dSolution(queenRow)
        else:
            # try to place the queen in each row in turn in this col,
            # and then recursively solve the rest of the columns
            for row in range(n):
                if isLegal(row,col):
                    queenRow[col] = row # place the queen and hope it works
                    solution = solve(col+1)
                    if (solution != None):
                        # ta da! it did work
                        return solution
                    queenRow[col] = -1 # pick up the wrongly-placed queen
            # shoot, can't place the queen anywhere
            return None
    return solve(0)

for n in range(1,10):
    print("n =", n)
    print(nQueens(n))
    print("******************************")