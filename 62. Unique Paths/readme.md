# 62. Unique Paths

## Problem
- A robot is located at the top-left corner of a m x n grid.
- The robot can only move either down or right at any point in time. 
- The robot is trying to reach the bottom-right corner of the grid.
- How many possible unique paths are there?

## Solution
```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
```

```python
class Solution(object):
    def uniquePaths(self, m, n):
        dp = [0] * n
        dp[0] = 1
        for _ in range(m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]
```
