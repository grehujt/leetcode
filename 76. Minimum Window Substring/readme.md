# 76. Minimum Window Substring

## Problem
- Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

> For example,
> S = "ADOBECODEBANC"
> T = "ABC"
> Minimum window is "BANC".

- If there is no such window in S that covers all characters in T, return the empty string "".
- If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

## Solution
[ref](https://discuss.leetcode.com/topic/20692/12-lines-python/18)
_The current window is s[i:j] and the result window is s[I:J]. In need[c] I store how many times I need character c (can be negative) and missing tells how many characters are still missing. In the loop, first add the new character to the window. Then, if nothing is missing, remove as much as possible from the window start and then update the result._

```python
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):  # [i:j)
            # Note: collections.Counter count of a missing element is zero
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if J == 0 or j-i < J-I:
                    I, J = i, j
        return s[I:J]
```

```python
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = [0]*256, len(t)  # use array instead of hash map
        for c in t: need[ord(c)] += 1
        i = I = J = 0
        for j, c in enumerate(s, 1):  # [i:j)
            missing -= need[ord(c)] > 0
            need[ord(c)] -= 1
            if not missing:
                while i < j and need[ord(s[i])] < 0:
                    need[ord(s[i])] += 1
                    i += 1
                if J == 0 or j-i < J-I:
                    I, J = i, j
        return s[I:J]
```
