## Longest Substring Without Repeating Characters

> Given a string, find the length of the longest substring without repeating characters.
>
> **Examples:**
>
> Given "abcabcbb", the answer is "abc", which the length is 3.
>
> Given "bbbbb", the answer is "b", with the length of 1.
>
> Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

---

**tips:**
> * dynamic programming
> * hash
> * 2 pointers
> * O(n)

---

## Solution

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastOccur = {}
        j, maxLen = 0, 0
        for i, c in enumerate(s):
            if c in lastOccur:
                j = max(j, lastOccur[c] + 1)
            lastOccur[c] = i
            maxLen = max(maxLen, i - j + 1)
        return maxLen
```
