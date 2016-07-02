# 14. Longest Common Prefix

## Problem
- Write a function to find the longest common prefix string amongst an array of strings.

## Solution

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1: return ''
        elif len(strs) == 1: return strs[0]
        s, i, jump = strs[0], 0, False
        while i < len(s):
            for j in xrange(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != s[i]:
                    jump = True
                    break
            if jump: break
            i += 1
        return strs[0][:i]
```
