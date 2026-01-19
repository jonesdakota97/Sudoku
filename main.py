import Input
import Algs.BruteForce as bruteForce
import Utils

solvedPuzzle = bruteForce.bruteForceFunc(Input.inputArr)

print('\n')
print('Solved:')
for row in solvedPuzzle:
    print(row)