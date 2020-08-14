def NextCell(grid, i, j):   ## Find the Index of the Grid ##
    for x in range(i,9):
        for y in range(j,9):
            if grid[x][y] == 0:
                return x,y
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == 0:
                return x,y
    return -1,-1

def isValid(grid, i, j, e):         ## Find whether the entered sudoku grid is valid to solve ##
    isRowOk = all([e != grid[i][i] for x in range(9)])      ## Validate the row ##
    if isRowOk:
        isColumnOk = all([e != grid[x][j] for x in range(9)])   ## Validate the Column ##
        if isColumnOk:
            secTopX, secTopY = 3*(i//3), 3*(j//3)              ## Main logic intials ##
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == 0:
                        return False
            return True
    return False
'''

solveSudoku()
This Function uses recurion to Solve the Sudoku Grid
It also acts as calling function

'''
def solveSudoku(grid, i=0, j=0):        ## Main Calling Function ##
    i,j = NextCell(grid, i, j)
    if i == -1:     ## If NextCell give indexing of end cell ##
        return True
    for e in range(1,10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid,i,j):   ## Recursion for Solving ##
                return True
            grid[i][j] = 0
    return False