# 67. Add Binary

## Prbolem
- Given two binary strings, return their sum (also a binary string).

> For example,
> 
> a = "11"
> 
> b = "1"
> 
> Return "100".

## Solution
```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]
```

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j, carry = len(a)-1, len(b)-1, 0
        ret = []
        while i >= 0 or j >= 0:
            d1 = ord(a[i])-ord('0') if i >= 0 else 0
            d2 = ord(b[j])-ord('0') if j >= 0 else 0
            tmp = d1+d2+carry
            if tmp > 1:
                ret.append('%d' % (tmp%2))
                carry = 1
            else:
                ret.append('%d' % tmp)
                carry = 0
            i -= 1
            j -= 1
        if carry == 1:
            ret.append('1')
        return ''.join(ret)[::-1]
```
