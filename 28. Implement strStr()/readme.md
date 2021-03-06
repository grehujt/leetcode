# 28. Implement strStr()

## Problem
- Implement strStr().
- Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

## Solution

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0: return 0
        if len(haystack) == 0: return -1
        m, n = len(haystack), len(needle)
        for i in xrange(m-n+1):
            for j in xrange(n+1):
                if j == n: return i
                if haystack[i+j] != needle[j]: break
        return -1
```
