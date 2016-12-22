# 64. Minimum Path Sum

## Problem
- Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
- Note: You can only move either down or right at any point in time.

## Solution
- O(mn) in time & space:
```python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0]*(n) for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
```

- O(mn) in time & space:
```python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[sys.maxint]*(n+1) for _ in range(m+1)]
        dp[0][1] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = grid[i-1][j-1] + min(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
```

- O(mn) in time, O(n) in space:
```python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [sys.maxint] * (n+1)  # dp[i] means min path sum for previous row to col i-1
        dp[1] = 0
        for i in range(1, m+1):
            dp[1] += grid[i-1][0]
            for j in range(2, n+1):
                dp[j] = grid[i-1][j-1] + min(dp[j-1], dp[j])
        return dp[-1]
```
