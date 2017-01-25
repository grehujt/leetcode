# 77. Combinations

## Problem
- Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

> For example,
> 
> If n = 4 and k = 2, a solution is:
> 
> [
> 
>   [2,4],
>   
>   [3,4],
>   
>   [2,3],
>   
>   [1,2],
>   
>   [1,3],
>   
>   [1,4],
>   
> ]

## Solution

TLE..
```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def _bt(ret, arr, used, i, last):
            if i == k:
                ret.append(copy.copy(arr))
                return
            for d in range(i, n):
                if used[d] == 0 and d > last:
                    arr[i] = d+1
                    used[d] = 1
                    _bt(ret, arr, used, i+1, d)
                    used[d] = 0
        ret = []
        _bt(ret,[0]*k, [0]*n, 0, -1)
        return ret
```

AC:
```python
class Solution(object):
    def combine(self, n, k):
        return list(itertools.combinations(range(1,n+1), k))
```
