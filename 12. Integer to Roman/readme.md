# 12. Integer to Roman

### Problem
- Given an integer, convert it to a roman numeral.
- Input is guaranteed to be within the range from 1 to 3999.

### Solution

```python
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # base cases
        sp = [(1,'I'), (4,'IV'), (5,'V'), (9,'IX'), (10,'X'), (40,'XL'), (50,'L'), (90,'XC'), (100,'C'), (400,'CD'), (500,'D'), (900,'CM'), (1000,'M')]
        curSp = len(sp)-1
        reslut = []
        while num > 0:  # till zero is reached
            # find the maximum base case for num
            while curSp >= 0 and num - sp[curSp][0] < 0:
                curSp -= 1
            # subtract num by the base case
            num -= sp[curSp][0]
            reslut.append(sp[curSp][1])
        return ''.join(reslut)
```
