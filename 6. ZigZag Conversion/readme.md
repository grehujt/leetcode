# 6. ZigZag Conversion

### Problem:

- The string _"PAYPALISHIRING"_ is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility):

```
P   A   H   N
A P L S I I G
Y   I   R
```

- And then read line by line: _"PAHNAPLSIIGYIR"_.

- Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string text, int nRows);
```

- convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

### Solution

- O(len(s)) in both time and space

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        arrs = [[] for i in range(numRows)]
        i, j, flag, length = 0, 0, True, len(s)
        while i < length:
            arrs[j].append(s[i])
            j = j+1 if flag else j-1
            if j==numRows or j<0:
                j = numRows-2 if flag else 1
                flag = not flag
            i += 1
        return ''.join(''.join(s) for s in arrs)
```

- O(len(s)) in time and space, 1 pass

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        tmp = []
        cycle = (numRows << 1) - 2
        for i in xrange(numRows):
            for j in xrange(i, len(s), cycle):
                tmp.append(s[j])
                nextJ = (j - i) + cycle - i
                if i!=0 and i!=numRows-1 and nextJ<len(s):
                    tmp.append(s[nextJ])
        return ''.join(tmp)
```
