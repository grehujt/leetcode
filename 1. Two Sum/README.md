## 1. Two sum

> Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.
>
> You may assume that each input would have **exactly** one solution.
> 
> **example:**
>
> '''
>
> Given nums = [2, 7, 11, 15], target = 9,
> 
> Because nums[**0**] + nums[**1**] = 2 + 7 = 9,
> 
> return **[0, 1]**.
>
> '''
>

---

INFO: please use **zero-based** indices.

> tips:
> * combination from itertools might be appealing to you, but indexOf has implicit loop
>
> * try to approach a O(n) time algorithm

---

## Solution

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n1 in enumerate(nums):
            n2 = target - n1
            if n2 in d:
                return [i, d[n2]]
            else:
                d[n1] = i
```