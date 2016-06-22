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

clever algorithm, which only needs half iterations:

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x!=0 and x%10==0): return False
        result = 0
        while result < x :
            result = result * 10 + (x % 10)
            x /= 10
        return result == x or result/10 == x
```
