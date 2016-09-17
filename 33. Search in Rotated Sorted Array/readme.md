# 33. Search in Rotated Sorted Array

## Problem
- Suppose a sorted array is rotated at some pivot unknown to you beforehand.
- (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
- You are given a target value to search.
- If found in the array return its index, otherwise return -1.
- You may assume no duplicate exists in the array.

## Solution
```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beg, end = 0, len(nums)-1
        if end == -1:
            return -1
        elif end == 0:
            return 0 if nums[0] == target else -1
        elif end == 1:
            if nums[0] == target: return 0
            elif nums[1] == target: return 1
            else: return -1

        while beg+1 < end:
            mid = (beg+end) >> 1
            if nums[mid] == target:
                return mid
            if nums[beg] > nums[mid]:
                end = mid
            elif nums[end] < nums[mid]:
                beg = mid
            else:
                beg, end = len(nums)-1, 0
                break

        if target > nums[beg] or target < nums[end]:
            return -1

        beg, end = (0, beg) if nums[0]<=target<=nums[beg] else (end, len(nums)-1)
        while beg <= end:
            mid = (beg+end) >> 1
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                end = mid-1
            else:
                beg = mid+1
        return -1
```

**key points:**
- find the rotation points in O(log(n))
- find the target using binary search in the proper section
