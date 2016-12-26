# 66. Plus One

## Problem
- Given a non-negative number represented as an array of digits, plus one to the number.
- The digits are stored such that the most significant digit is at the head of the list.

## Solution
```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        ret = []
        for i in range(len(digits)-1, -1, -1):
            d = digits[i]
            if d+carry > 9:
                ret.append(0)
                carry = 1
            else:
                ret.append(d+carry)
                carry = 0
        if carry == 1:
            ret.append(1)
        ret.reverse()
        return ret
```
