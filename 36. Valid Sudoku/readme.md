# 36. Valid Sudoku

## Problem
- Determine if a Sudoku is valid:
    + Each row must have the numbers 1-9 occuring just once.
    + Each column must have the numbers 1-9 occuring just once.
    + And the numbers 1-9 must occur just once in each of the 9 sub-boxes of the grid.
- The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
- A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

## Solution
```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            rowSet, colSet, gridSet = set(), set(), set()
            for j in range(9):
                colItem = board[i][j]
                rowItem = board[j][i]
                gridItem = board[i/3*3+j/3][(i%3)*3+j%3]
                if (colItem!='.' and colItem in colSet) or (rowItem!='.' and rowItem in rowSet) or (gridItem!='.' and gridItem in gridSet):
                    return False
                rowSet.add(rowItem)
                colSet.add(colItem)
                gridSet.add(gridItem)
        return True
```
