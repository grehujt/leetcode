# 70. Climbing Stairs

## Problem
- You are climbing a stair case. It takes n steps to reach to the top.
- Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Solution
```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        while n:
            a, b = b, a+b
            n -= 1
        return a
```
