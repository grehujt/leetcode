# 52. N-Queens II

## Problem
- Follow up for N-Queens problem. Now, instead outputting board configurations, return the total number of distinct solutions.

## Solution
```python
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                self.ret += 1
                return
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    DFS(queens+[q], xy_dif|set([p-q]), xy_sum|set([p+q]))  ## memery consumption
        self.ret = 0
        DFS([], set(), set())
        return self.ret
```
