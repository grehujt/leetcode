# 42. Trapping Rain Water

## Problem
- Given n non-negative integers representing an elevation map where the width of each bar is 1,
- compute how much water it is able to trap after raining.

> Example:
> 
> Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

![pic](pic.png)

## Solution I with 2 pointers
```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n, ret = len(height), 0
        lh, rh = [0]*n, [0]*n
        for i in xrange(1, n):
            lh[i] = max(lh[i-1], height[i-1])
        for i in xrange(n-2, -1, -1):
            rh[i] = max(rh[i+1], height[i+1])
            minH = min(lh[i], rh[i])
            ret += minH-height[i] if minH>height[i] else 0
        return ret
```

## Solution II with stack
```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def calc(curItem, maxH, stack):
            ret = 0
            i, h = curItem
            if stack:
                if h >= maxH:
                    while stack:
                        lastI, lastH = stack.pop()
                        ret -= lastH
                    tmp = min(lastH, h) * (i-lastI)
                    ret += tmp if tmp!=0 else lastH
            return ret

        stack = []
        result, maxH = 0, -1
        for i, h in enumerate(height):
            result += calc((i, h), maxH, stack)
            maxH = max(h, maxH)
            stack.append((i, h))
        if stack:
            result += calc(stack.pop(), h, stack[::-1])
        return result
```
