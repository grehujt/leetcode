# 50. Pow(x, n)

## Problem
- Implement pow(x, n).

## Solution
```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def calc(x, n):
            if n == 0: return 1
            ret = calc(x, n>>1)
            ret *= ret
            ret *= x if n & 1 else 1
            return ret
        if n > 0: 
            return calc(x, n)
        elif n < 0: 
            return 1.0 / calc(x, -n)
        else: 
            return 1
```
