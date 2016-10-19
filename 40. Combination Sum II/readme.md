# 40. Combination Sum II

## Problem
- Given a collection of candidate numbers (C) and a target number (T), 
- find all unique combinations in C where the candidate numbers sums to T.
- Each number in C may only be used __once__ in the combination.
- All numbers (including target) will be positive integers.
- The solution set must not contain duplicate combinations.

> For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
> 
> A solution set is: 
> 
> [
> 
>   [1, 7],
>   
>   [1, 2, 5],
>   
>   [2, 6],
>   
>   [1, 1, 6]
>   
> ]

## Solution
```python
class Solution(object):
    def combinationSum2(self, candidates, target):
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
                    if i!=beg and d==candidates[i-1]:
                        continue
                    tmp.append(d)
                    if t-d < 0:
                        tmp.pop()
                        return
                    else:
                        bt(i+1, t-d, tmp)
                        tmp.pop()

        result = []
        candidates.sort()
        bt(0, target, [])
        return result
```
