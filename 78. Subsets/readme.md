# 78. Subsets

## Problem
- Given a set of distinct integers, nums, return all possible subsets.
- Note: The solution set must not contain duplicate subsets.

> For example,
> 
> If nums = [1,2,3], a solution is:
> 
> [
>   [3],
>   
>   [1],
>   
>   [2],
>   
>   [1,2,3],
>   
>   [1,3],
>   
>   [2,3],
>   
>   [1,2],
>   
>   []
>   
> ]

## Solution
```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[], nums]
        for i in xrange(len(nums)-1):
            ret.extend(list(l) for l in itertools.combinations(nums, i+1))
        return ret
```

[ref](https://discuss.leetcode.com/topic/19561/python-easy-to-understand-solutions-dfs-recursively-bit-manipulation-iteratively/2)
DFS:
```python
class Solution(object):
    def subsets(self, nums):
        def _dfs(ret, arr, beg):
            ret.append(arr)
            for i in range(beg, len(nums)):
                _dfs(ret, arr+[nums[i]], i+1)
        ret = []
        _dfs(ret, [], 0)
        return ret
```

[ref](https://discuss.leetcode.com/topic/19561/python-easy-to-understand-solutions-dfs-recursively-bit-manipulation-iteratively/2)
Iterative:
```python
class Solution(object):
    def subsets(self, nums):
        ret = [[]]
        for n in nums:
            ret += [l+[n] for l in ret]
        return ret
```
