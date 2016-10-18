# 39. Combination Sum

## Problem
- Given a set of candidate numbers (C) and a target number (T),
- find all unique combinations in C where the candidate numbers sums to T.
- The __same__ repeated number may be chosen from C __unlimited__ number of times.
- All numbers (including target) will be positive integers.
- The solution set must not contain duplicate combinations.

> For example, given candidate set [2, 3, 6, 7] and target 7,
> 
> A solution set is: 
> 
> [
> 
>   [7],
>   
>   [2, 2, 3]
>   
> ]

## Solution
```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def bt(beg, t, tmp):
            if t == 0:
                result.append([x for x in tmp])
            else:
                for i in xrange(beg, len(candidates)):
                    d = candidates[i]
                    tmp.append(d)
                    if t-d < 0:
                        tmp.pop()
                        return
                    else:
                        bt(i, t-d, tmp)
                        tmp.pop()

        result = []
        candidates.sort()
        bt(0, target, [])
        return result
```

