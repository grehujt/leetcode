# 13. Roman to Integer

### Problem
- Given a roman numeral, convert it to an integer.
- Input is guaranteed to be within the range from 1 to 3999.

### Solution

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sp = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        pre, result = 4000, 0
        for c in s:
            # take care of minus cases
            result += sp[c] if pre>=sp[c] else sp[c]-(pre<<1)
            pre = sp[c]
        return result
```

**milestone**

![time dist](./pic.png)