# 69. Sqrt(x)

## Problem
- Implement int sqrt(int x).
- Compute and return the square root of x.

## Solution
```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        beg, end = 0, x
        while beg+1 < end:
            mid = (beg+end) >> 1
            if mid*mid == x: return mid
            beg, end = (beg, mid) if mid*mid > x else (mid, end)
        return end if end*end <= x else beg
```

Newton's method:
```python
class Solution(object):
    def mySqrt(self, x):
        ret = x
        while ret*ret > x:
            ret = (ret + x/ret) >> 1
        return ret
```
