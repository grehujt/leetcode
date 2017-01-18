# 75. Sort Colors

## Problem
- Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
- Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
- You are not suppose to use the library's sort function for this problem.
- an one-pass algorithm using only constant space.

## Solution
```python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, 0
        for n in nums:
            nums[b] = 2
            b += 1
            if n < 2:
                nums[w] = 1
                w += 1
            if n < 1:
                nums[r] = 0
                r += 1
```

_Dutch national flag problem_
_three-way-partition_
```python
class Solution(object):
    def sortColors(self, nums):
        left, i, right = 0, 0, len(nums)-1
        while i <= right:
            if nums[i] < 1:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] > 1: # i not increase, might not be strict one-pass
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
```
