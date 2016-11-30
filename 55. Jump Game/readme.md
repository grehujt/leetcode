# 55. Jump Game

## Problem
- Given an array of non-negative integers, you are initially positioned at the first index of the array.
- Each element in the array represents your maximum jump length at that position.
- Determine if you are able to reach the last index.

> For example:
> 
> A = [2,3,1,1,4], return true.
> 
> A = [3,2,1,0,4], return false.

## Solution
```python
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n, maxR = len(nums), 0
        for i in xrange(n):
            if i > maxR: return False
            maxR = max(maxR, i+nums[i])
        return True
```
