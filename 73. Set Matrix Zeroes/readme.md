# 73. Set Matrix Zeroes

## Problem
- Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
- Do it in place.
- O(1) space complexity.

## Solution
```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # put stat at the beg of row/col
        m, n, col0 = len(matrix), len(matrix[0]), 1
        for i in range(m):
            if matrix[i][0] == 0: col0 = 0
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # load reversely
        for i in range(m-1, -1, -1):
            for j in range(n-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
```
