# 11. Container With Most Water

### Problem
- Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
- n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
- Find two lines, which together with x-axis forms a container, such that the container contains the most water.
- Note: You may not slant the container.

### Solutions

- O(n^2):

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2: return 0
        maxArea = 0
        for i in xrange(len(height)):
            for j in xrange(i+1, len(height)):
                maxArea = max(maxArea, (j-i)*height[j] if height[j]<height[i] else (j-i)*height[i])
        return maxArea
```

TLE..

