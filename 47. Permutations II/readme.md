# 47. Permutations II

## Problem
- Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

## Solution
```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def bt(ret, tmpArr, used, n):
            if n == len(nums):
                ret.append(copy.copy(tmpArr))
                return
            for i, x in enumerate(nums):
                if used[i] or (i>0 and not used[i-1] and nums[i-1]==nums[i]):
                    continue
                used[i] = True
                tmpArr[n] = x
                bt(ret, tmpArr, used, n+1)
                used[i] = False
        ret, n = [], len(nums)
        nums.sort()
        bt(ret, [0]*n, [False]*n, 0)
        return ret
```
