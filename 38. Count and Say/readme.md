# 38. Count and Say

## Problem
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the n-th sequence.

__Note:__ The sequence of integers will be represented as a string.

## Solution I
```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        for _ in xrange(n-1):
            tmp, pre, cnt = [], result[0], 0
            for i in xrange(len(result)):
                if result[i] == pre:
                    cnt += 1
                else:
                    tmp.append('%d%s' % (cnt, pre))
                    pre = result[i]
                    cnt = 1
                if i == len(result)-1:
                    tmp.append('%d%s' % (cnt, pre))
            result = ''.join(tmp)
        return result
```

# Solution II
```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        pre, cur = '', '1'
        for _ in xrange(n-1):
            pre, cur, cnt = cur, '', 1
            for i in xrange(len(pre)):
                if i+1<len(pre) and pre[i]==pre[i+1]:
                    cnt += 1
                else:
                    cur = '%s%d%s' % (cur, cnt, pre[i])
                    cnt = 1
        return cur
```
