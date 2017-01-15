# 74. Search a 2D Matrix

## Problem
- Write an efficient algorithm that searches for a value in an m x n matrix. 
- This matrix has the following properties:
    + Integers in each row are sorted from left to right.
    + The first integer of each row is greater than the last integer of the previous row.

> For example, consider the following matrix:
> 
> [
> 
>   [1,   3,  5,  7],
>   
>   [10, 11, 16, 20],
>   
>   [23, 30, 34, 50]
>   
> ]
> 
> Given target = 3, return true.

## Solution
```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix and matrix[0]:
            an0 = bisect.bisect([arr[0] for arr in matrix], target)
            if matrix[an0-1][0] == target:
                return True
            an1 = bisect.bisect(matrix[an0-1], target)
            if matrix[an0-1][an1-1] == target:
                return True
        return False
```

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix and matrix[0]:
            m, n = len(matrix), len(matrix[0])
            beg, end = 0, m*n-1
            while beg <= end:
                mid = (beg + end) >> 1
                num = matrix[mid/n][mid%n]
                if num == target:
                    return True
                if num > target:
                    end = mid-1
                else:
                    beg = mid+1
        return False
```
