# 16. 3Sum Closest

## Problem
- Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
- Return the sum of the three integers.
- You may assume that each input would have exactly one solution.

> For example, given array S = {-1 2 1 -4}, and target = 1.
> The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

## Solution

Same idea as problem 15:

```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        minDiff, minS = sys.maxint, None
        nums.sort()
        keys = nums
        for i in xrange(len(keys) - 2):
            if i != 0 and keys[i] == keys[i-1]:
                continue
            n1 = keys[i]
            j, k = i + 1, len(keys) - 1
            while j < k:
                n2, n3 = keys[j], keys[k]
                s = n1 + n2 + n3
                d = abs(s - target)
                if d == 0:
                    return s
                if minDiff > d:
                    minDiff = d
                    minS = s
                if s < target:
                    j += 1
                    while j < k and keys[j] == keys[j-1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and keys[k] == keys[k+1]:
                        k -= 1
        return minS
```
