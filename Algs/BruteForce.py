import Utils
import copy

#input will be a 2D array of integers
def bruteForceFunc(input, rowStartIndex = 0, colStartIndex = 0, valToTry = 1):
    puzzleCopy = copy.deepcopy(input)
    
    n = len(input)
    for row in range(rowStartIndex, n):
        for col in range(colStartIndex, n):
            if (valToTry > n):
                return puzzleCopy
            if (puzzleCopy[row][col] > 0):
                continue
            
            if (Utils.isInCol(puzzleCopy, col, valToTry) or
                Utils.isInRow(puzzleCopy, row, valToTry) or
                Utils.isInSquare(puzzleCopy, row, col, valToTry)):
                puzzleCopy = bruteForceFunc(puzzleCopy, rowStartIndex, colStartIndex, valToTry+1 )
            else:
                puzzleCopy[row][col] = valToTry
                print('\n')
                for r in puzzleCopy:
                    print(r)
                print('\n')
                puzzleCopy = bruteForceFunc(puzzleCopy, row, col, valToTry+1)

    return puzzleCopy