# 54. Spiral Matrix

## Problem
- Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix **in spiral order**.

> For example,
> 
> Given the following matrix:
> 
> [
> 
>  [ 1, 2, 3 ],
>  
>  [ 4, 5, 6 ],
>  
>  [ 7, 8, 9 ]
>  
> ]
> 
> You should return [1,2,3,6,9,8,7,4,5].

## Solution
```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0]) if len(matrix)>0 else 0
        t, r, b, l, ret = 0, 0, 0, 0, []
        while 1:
            for i in range(l, n-r):
                ret.append(matrix[t][i])
            t += 1
            if t + b >= m:
                break
            for i in range(t, m-b):
                ret.append(matrix[i][n-r-1])
            r += 1
            if l + r >= n:
                break
            for i in range(n-r-1, l-1, -1):
                ret.append(matrix[m-b-1][i])
            b += 1
            if t + b >= m:
                break
            for i in range(m-b-1, t-1, -1):
                ret.append(matrix[i][l])
            l += 1
            if l + r >= n:
                break
        return ret
```