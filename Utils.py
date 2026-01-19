import math

def isInRow(puzzle, rowIndex, val, excludeCol = -1):
    isInRow = False
    for col in range(len(puzzle[rowIndex])):
        if col != excludeCol and puzzle[rowIndex][col] == val:
            isInRow = True
    return isInRow

def isInCol(puzzle, colIndex, val, excludedRow = -1):
    isInCol = False
    for row in range(len(puzzle)):
        if excludedRow != row and puzzle[row][colIndex] == val:
            isInCol = True
    return isInCol

# indexes of squares should be horizontal first, then vertical. I.E:
#   0, 1, 2
#   3, 4, 5
#   6, 7, 8
def isInSquare(puzzle, rowIndex, colIndex, val):
    isInSquare = False
    sqrtOfN = math.floor(math.sqrt(len(puzzle)))
    rowMultiplier = math.floor(rowIndex/sqrtOfN)
    colMultiplier = math.floor(colIndex/sqrtOfN)
    startingRow = math.floor(sqrtOfN * rowMultiplier)
    startingCol = math.floor(sqrtOfN * colMultiplier)

    for r in range(sqrtOfN):
        for c in range(sqrtOfN):
            if (startingRow + r != rowIndex and 
                startingCol + c != colIndex and 
                puzzle[startingRow + r][startingCol + c] == val):                
                isInSquare = True
    return isInSquare

def canBeVal(puzzle, row, col, val):
    return (not (isInCol(puzzle, col, val) or
            isInRow(puzzle, row, val) or
            isInSquare(puzzle, row, col, val)))

def isSolved(puzzle):
    isSolved = True
    for row in range(len(puzzle)):
        for col in range(row):
            if (puzzle[row][col] == 0):
                isSolved = False
            elif (isInCol(puzzle, col, puzzle[row][col], row) or
                  isInRow(puzzle, row, puzzle[row][col], col) or 
                  isInSquare(puzzle, row, col, puzzle[row][col])):
                isSolved = False

    return isSolved