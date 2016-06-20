# 7. Reverse Integer

### Problem:

- Reverse digits of an integer.

- Example 1: x = 123, return 321.

- Example 2: x = -123, return -321.

- check overflow.

---

### Solution:

```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = True if x < 0 else False
        x = -x if isNegative else x
        result = 0
        while x > 0:
            result = result * 10 + (x % 10)
            if result > 0x7fffffff:
                return 0
            x /= 10
        return -result if isNegative else result
```
