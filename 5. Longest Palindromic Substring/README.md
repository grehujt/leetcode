## 5. Longest palindromic Substring

- Give a string S, find the longest palindromic substring in S.
- Maximum length of S is 1000.
- There exists one unique longest palindromic substring.

---

### Analysis

1. Brute-force, iterate all possible substring, **O(n^3)**, 100% TLE.

2. Dynamice programming, use a 2d boolean array dp, if dp[i][j] == True, then s[i:j+1] is palindromic. In this case, we have to iterate all possible length of substring as well as starting points, so it is a **O(n^2)** solution.

    ```python
    class Solution(object):
        def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: str
            """
            length = len(s)
            if length < 2:
                return s
            dp = [[False] * length for ss in s]
            dp[0][0] = True
            for i in xrange(1, length):
                dp[i][i] = True
                # takes care of length of 2
                dp[i][i-1] = True
            l, r = 0, 0
            for j in xrange(2, length+1):
                for i in xrange(length-j+1):
                    if s[i] == s[i+j-1] and dp[i+1][i+j-2]:
                        dp[i][i+j-1] = True
                        if r-l < j:
                            l = i
                            r = i+j-1
            return s[l:r+1]
    ```
    
    But it still gets TLE...

3. O(n) solution
    I thought solving this in O(nlog(n)) was the best until I found a O(n), which is called [Manacher’s Algorithm](http://articles.leetcode.com/longest-palindromic-substring-part-ii). My implementation in python:

    ```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        newS = '#%s#' % '#'.join(s)
        length, center, rightMost, maxCenter, maxLen, i = len(newS), 0, 0, 0, 0, 0
        pArr = [0] * length
        while i < length:
            pArr[i] = 1 if rightMost < i else min(rightMost-i, pArr[(center << 1) - i])
            while i + pArr[i] < length and i - pArr[i] > -1 and newS[i + pArr[i]] == newS[i - pArr[i]]:
                pArr[i] += 1
            if i + pArr[i] > rightMost:
                center = i
                rightMost = i + pArr[i]
                if pArr[i] > maxLen:
                    maxLen = pArr[i]
                    maxCenter = i
            i += 1
        start = (maxCenter - maxLen + 1) >> 1
        return s[start: start + maxLen - 1]
    ```

    [some more algorithms](https://leetcode.com/articles/longest-palindromic-substring/).
