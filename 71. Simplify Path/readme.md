# 71. Simplify Path

## Problem
- Given an absolute path for a file (Unix-style), simplify it.

> For example,
> 
> path = "/home/", => "/home"
> 
> path = "/a/./b/../../c/", => "/c"

## Solution
```python
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ret = []
        for item in path.split('/'):
            if item and item != '.':
                if ret and item == '..':
                    ret.pop()
                elif item != '..':
                    ret.append(item)
        return '/%s' % '/'.join(ret)
```
