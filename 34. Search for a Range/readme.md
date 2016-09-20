# 34. Search for a Range

## Problem
- Given a sorted array of integers, find the starting and ending position of a given target value.
- Your algorithm's runtime complexity must be in the order of O(log n).
- If the target is not found in the array, return [-1, -1].

> For example,
> 
> Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].

## Solution
```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def _binary_search(beg, end, t):
            while beg < end:
                mid = beg + ((end-beg) >> 1)
                if nums[mid] < t:
                    beg = mid+1
                else:
                    end = mid
            return beg

        idx = _binary_search(0, len(nums), target)
        if idx==len(nums) or nums[idx]!=target:
            return [-1, -1]
        else:
            return [idx, _binary_search(idx+1, len(nums), target+1) - 1]
```
