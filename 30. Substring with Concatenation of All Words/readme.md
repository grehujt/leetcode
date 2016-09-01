# 30. Substring with Concatenation of All Words

## Problem
- You are given a string, s, and a list of words, words, that are all of the same length.
- Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

> For example, given:
> s: "barfoothefoobarman"
> words: ["foo", "bar"]
> 
> You should return the indices: [0,9].
> (order does not matter).

## Solution
```python
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        d1 = {}
        for w in words:
            if w not in d1:
                d1[w] = 1
            else:
                d1[w] += 1
        singleLen, wordsCnt = len(words[0]), len(words)
        result = []
        for i in xrange(len(s) - singleLen * wordsCnt + 1):
            d2 = {}
            j = 0
            while j < wordsCnt:
                key = s[i+j*singleLen:i+(j+1)*singleLen]
                if key not in d1:  ## optimization space!!
                    break
                if key not in d2:
                    d2[key] = 1
                else:
                    d2[key] += 1
                    if d2[key] > d1[key]:
                        break
                j += 1
            if j == wordsCnt:
                result.append(i)
        return result
```
