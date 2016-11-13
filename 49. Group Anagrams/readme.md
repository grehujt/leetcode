# 49. Group Anagrams

## Problem
- Given an array of strings, group anagrams together.

> For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
> 
> Return:
> 
> [
> 
>   ["ate", "eat","tea"],
>   
>   ["nat","tan"],
>   
>   ["bat"]
>   
> ]

- Note: All inputs will be in lower-case.

## Solution
```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            k = ''.join(sorted(s))
            if k not in d:
                d[k] = [s]
            else:
                d[k].append(s)
        return d.values()
```
