"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, 
each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.array.integer grid

    A matrix representing 9 × 9 grid already filled with numbers from 1 to 9.

    [output] boolean

    true if the given grid represents a correct solution to Sudoku, false otherwise.
"""

def sudoku(grid):
  # validate rows, if any non unique elements exist, then return False 
  for i in [set(i) for i in grid]:
    if len(i) != 9:
      return False
  # validate columns, if any non unique elements exist, then return False 
  cols = []
  for i in range(9):
    colSum = []
    for j in range(9):
      colSum.append(grid[j][i])
    cols.append(set(colSum))
  for i in cols:
    if len(i) != 9:
      return False
  
  # Validate each 3x3 matrix, if sum of matrix != 45 (max possible sum) then return False
  mStart = stepStart = 0
  mEnd = stepEnd = 3
  currentMatrixQty = 0
  while currentMatrixQty != 9:
    matrix = []
    currentMatrixQty += 1
    for i in range(stepStart, stepEnd):
      matrix.append(sum(grid[i][mStart:mEnd]))
    if sum(matrix) != 45:
      return False
    if mEnd == 9:
      stepStart = stepEnd
      stepEnd += 3
      mStart = 0
      mEnd = 3
    else:
      mEnd += 3
      mStart += 3
  return True
