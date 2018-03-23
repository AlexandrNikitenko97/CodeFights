"""
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

    For cell1 = "A1" and cell2 = "C3", the output should be
    chessBoardCellColor(cell1, cell2) = true.

    For cell1 = "A1" and cell2 = "H3", the output should be
    chessBoardCellColor(cell1, cell2) = false.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string cell1

    [input] string cell2

    [output] boolean

    true if both cells have the same color, false otherwise.
"""

from string import ascii_uppercase as ascii

def chessBoardCellColor(cell1, cell2):
    letters = ascii[:8]
    numbers = list(range(1,9))
    board = {}
    row = 0
    for i in numbers:
        cell = 0
        row += 1
        for j in letters:
            if row % 2 == 0:
                if cell % 2 == 0:
                    board[j + str(i)] = 'white'
                else:
                    board[j + str(i)] = 'black'
            else:
                if cell % 2 == 0:
                    board[j + str(i)] = 'black'
                else:
                    board[j + str(i)] = 'white'
            cell += 1
    return board[cell1] == board[cell2]
