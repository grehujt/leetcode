# 35. Search Insert Position

## Problem
- Given a sorted array and a target value, return the index if the target is found.
- If not, return the index where it would be if it were inserted in order.
- You may assume no duplicates in the array.

> Here are few examples.
> 
> [1,3,5,6], 5 → 2
> 
> [1,3,5,6], 2 → 1
> 
> [1,3,5,6], 7 → 4
> 
> [1,3,5,6], 0 → 0

## Solution
- if no duplicate exists, normal binary search would solve the problem.

**the following code handles duplicates as well:**
```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def _search(lo, hi):
            while lo <= hi:
                mid = lo + ((hi-lo) >> 1)
                if nums[mid] < target:
                    lo = mid+1
                else:
                    hi = mid-1
            return lo
        return _search(0, len(nums)-1)
```
