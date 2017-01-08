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
        # dp[i][j]: min # of steps for word1[:i] coverting to word2[:j]
        # dp[i][j] = min (
        #   1. insert, dp[i][j-1] + 1
        #   2. delete, dp[i-1][j] + 1
        #   3. replace, dp[i-1][j-1] + (1 if w1[i-1]!=w2[j-1] else 0)
        # )

```
