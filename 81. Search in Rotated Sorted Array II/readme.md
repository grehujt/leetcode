# 81. Search in Rotated Sorted Array II

## Problem
- Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

> - (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

- Write a function to determine if a given target is in the array.
- The array may contain duplicates.

## Solution
```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def _find_max(beg, end):
            if beg == end: return beg
            mid = (beg+end) >> 1
            if beg+1 == end:
                return beg if nums[beg] > nums[end] else None
            elif nums[beg] < nums[mid] > nums[end]:
                return _find_max(beg+1, end)
            else:
                ret = _find_max(beg, mid)
                return ret if ret is not None else _find_max(mid, end)
                # wrong statement, _find_max can return zero
                # return _find_max(beg, mid) or _find_max(mid, end)

        def _binary_search(beg, end):
            while beg <= end:
                mid = (beg+end) >> 1
                if target == nums[mid]:
                    return True
                elif target > nums[mid]:
                    beg = mid+1
                else:
                    end = mid-1
            return False

        if nums:
            an = _find_max(0, len(nums)-1)
            if an is not None:
                if target == nums[an]: return True
                if target > nums[an]: return False
                return _binary_search(0, an) or _binary_search(an+1, len(nums)-1)
            else:
                return _binary_search(0, len(nums)-1)
        return False
```

[ref](https://discuss.leetcode.com/topic/310/when-there-are-duplicates-the-worst-case-is-o-n-could-we-do-better)
```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        beg, end = 0, len(nums)-1
        while beg <= end:
            if nums[beg] == target or nums[end] == target: return True
            mid = (beg+end) >> 1
            if nums[mid] == target: return True
            if nums[beg] < nums[mid]:  # beg..mid is sorted
                if nums[beg] < target < nums[mid]:
                    end = mid-1
                else:
                    beg = mid+1
            elif nums[beg] > nums[mid]:  # mid..end is sorted
                if nums[mid] < target < nums[end]:
                    beg = mid+1
                else:
                    end = mid-1
            else:
                beg += 1
        return False
```
