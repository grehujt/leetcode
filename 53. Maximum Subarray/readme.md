# 53. Maximum Subarray

## Problem
- Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

> For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
> 
> the contiguous subarray [4,-1,2,1] has the largest sum = 6.

## Solution
```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        continuousSum, maxSoFar = nums[0], nums[0]
        sumMin = min(0, continuousSum)
        for i in range(1, len(nums)):
            continuousSum += nums[i]
            maxSoFar = max(maxSoFar, continuousSum-sumMin)
            sumMin = min(sumMin, continuousSum)
        return maxSoFar
```

**ref:[here](https://discuss.leetcode.com/topic/3400/simplest-and-fastest-o-n-c-solution)**
```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        continuousSum, maxSoFar = 0, nums[0]
        for n in nums:
            continuousSum += n
            maxSoFar = max(maxSoFar, continuousSum)
            continuousSum = max(continuousSum, 0)
        return maxSoFar
```

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preMax = curMax = nums[0]
        for i in range(1, len(nums)):
            preMax = max(preMax+nums[i], nums[i])
            curMax = max(curMax, preMax)
        return curMax
```
