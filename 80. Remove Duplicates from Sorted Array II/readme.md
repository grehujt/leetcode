# 80. Remove Duplicates from Sorted Array II

## Problem
- Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

> For example,
> Given sorted array nums = [1,1,1,2,2,3],
> 
> Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

## Solution
```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2: return len(nums)
        i, j = 1, 2
        while j < len(nums):
            nums[i+1] = nums[j]
            i += nums[i] != nums[j] or nums[i-1] != nums[i]
            j += 1
        return i+1
```

[ref](https://discuss.leetcode.com/topic/17180/3-6-easy-lines-c-java-python-ruby/2)
```python
class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
```
