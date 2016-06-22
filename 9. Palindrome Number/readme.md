# 9. Palindrome Number

### Problem
- Determine whether an integer is a palindrome.
- O(1) space at most.

### Solution

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        result = x % 10
        t = x / 10
        while t > 0:
            result = result * 10 + (t % 10)
            t /= 10
        return result == x
```


