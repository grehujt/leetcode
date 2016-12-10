# 60. Permutation Sequence

## Problem
- The set [1,2,3,…,n] contains a total of n! unique permutations.

- By listing and labeling all of the permutations in order, We get the following sequence (ie, for n = 3):

> "123"
> 
> "132"
> 
> "213"
> 
> "231"
> 
> "312"
> 
> "321"

- Given n and k, return the kth permutation sequence.
- Note: Given n will be between 1 and 9 inclusive.

## Solution

Note: Using backtracking will get TLE..

```python
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        facs = [1] * n
        for i in range(2, n):
            facs[i] = i * facs[i-1]
        nums = range(1, n+1)
        ret, k = [], k-1
        for i in range(1, n+1):
            idx = k / facs[n-i]
            ret.append(nums.pop(idx))
            k -= idx * facs[n-i]
        return ''.join(str(i) for i in ret)
```
