# 27. Remove Element

## Problem
- Given an array and a value, remove all instances of that value in place and return the new length.
- Do not allocate extra space for another array, you must do this in place with constant memory.
- The order of elements can be changed. It doesn't matter what you leave beyond the new length.


## Solution

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j, n = 0, 0, len(nums)
        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
```

Note that the following solution is taken from [here](https://leetcode.com/articles/remove-element/).

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n
```
