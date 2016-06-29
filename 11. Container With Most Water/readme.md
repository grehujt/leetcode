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

- O(n) DP solution:

    + The area between height[i] and height[j] (j>i) can be derived by: min(height[i], height[j]) * (j - i).

    + Let dp[l][r] represent max area from height[l:r+1], and clearly dp[l][r] is maximum of:
        1. dp[l+1][r], if height[l] < height[r], in this case height[l] is the bottleneck.
        2. Likewise, dp[l][r-1], if height[l] > height[r]. If height[l] == height[r], dp[l+1][r] == dp[l][r-1], we can combine this case to either case 1 or case 2.
        3. dp[l][r], clearly is one possibility.


```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2: return 0
        l, r, largest = 0, len(height)-1, -1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            largest = max(area, largest)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return largest
```

Accelerated version by skipping impossible cases:

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2: return 0
        l, r, largest = 0, len(height)-1, -1
        while l < r:
            heightL, heightR = height[l], height[r]
            area = min(heightL, heightR) * (r - l)
            largest = max(area, largest)
            if heightL < heightR:
                l += 1
                while height[l+1] < heightL:  # skip impossible case
                    l += 1
            else:
                r -= 1
                while height[r-1] < heightR:  # skip impossible case
                    r -= 1
        return largest
```