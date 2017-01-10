# 72. Edit Distance

## Problem
- Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

- You have the following 3 operations permitted on a word:
    + Insert a character
    + Delete a character
    + Replace a character

## Solution
```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp[i][j]: min # of steps for word1[:i+1] coverting to word2[:j+1]
        # dp[i][j] = min (
        #   1. insert, dp[i][j-1] + 1
        #   2. delete, dp[i-1][j] + 1
        #   3. replace, dp[i-1][j-1] + (1 if w1[i-1]!=w2[j-1] else 0)
        # )
        m, n = len(word1)+1, len(word2)+1
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = i
        for i in range(n):
            dp[0][i] = i
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j-1]+1,
                            dp[i-1][j]+1,
                            dp[i-1][j-1]+(1 if word1[i-1]!=word2[j-1] else 0))
        return dp[-1][-1]
```

O(n) space version (column-based):
```python
class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1)+1, len(word2)+1
        dp = [0] * n
        for i in range(n):
            dp[i] = i
        for i in range(1, m):
            pre = dp[0]
            dp[0] = i
            for j in range(1, n):
                tmp = dp[j]
                dp[j] = min(dp[j-1]+1,
                            dp[j]+1,
                            pre+(1 if word1[i-1]!=word2[j-1] else 0))
                pre = tmp
        return dp[-1]
```

O(m) space version (row-based):
```python
class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1)+1, len(word2)+1
        dp = [0] * m
        for i in range(m):
            dp[i] = i
        for i in range(1, n):
            pre = dp[0]
            dp[0] = i
            for j in range(1, m):
                tmp = dp[j]
                dp[j] = min(dp[j-1]+1,
                            dp[j]+1,
                            pre+(1 if word1[j-1]!=word2[i-1] else 0))
                pre = tmp
        return dp[-1]
```
