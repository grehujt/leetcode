# 18. 4Sum

## Problem
- Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target.
- Find all unique quadruplets in the array which gives the sum of target.
- The solution set must not contain duplicate quadruplets.

> For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
> 
> A solution set is:
> 
> [
> 
>   [-1,  0, 0, 1],
>   
>   [-2, -1, 1, 2],
>   
>   [-2,  0, 0, 2]
>   
> ]

## Solution

- O(n^3) accelerated ver:

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        if nums[0] << 2 > target or nums[-1] << 2 < target:
            return []
        result = []
        for i in xrange(len(nums)-3):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            n1 = nums[i]
            if n1 + 3*nums[-1] < target:
                continue
            if n1 << 2 > target:
                break
            if n1 << 2 == target:
                if n1 == nums[i+3]:
                    result.append(nums[i:i+4])
                break
            for j in xrange(i+1, len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                n2 = nums[j]
                if n1 + n2 + (nums[-1] << 1) < target:
                    continue
                if n1 + 3*n2 > target:
                    break
                l, r = j+1, len(nums)-1
                while l < r:
                    n3, n4 = nums[l], nums[r]
                    if n4 << 2 < target or n1+n2+(n3<<1) > target:
                        break
                    s = n1+n2+n3+n4
                    if s == target:
                        result.append([n1, n2, n3, n4])
                        l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s > target:
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    else:
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
        return result
```

