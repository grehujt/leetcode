# 42. Trapping Rain Water

## Problem
- Given n non-negative integers representing an elevation map where the width of each bar is 1,
- compute how much water it is able to trap after raining.

> Example:
> 
> Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

![pic](pic.png)

## Solution
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
