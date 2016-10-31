# 44. Wildcard Matching

## Problem
- Implement wildcard pattern matching with support for '?' and '*'.

- '?' Matches any single character.
- '*' Matches any sequence of characters (including the empty sequence).

- The matching should cover the entire input string (not partial).

- The function prototype should be:
    bool isMatch(const char *s, const char *p)

> Some examples:
> 
> isMatch("aa","a") → false
> 
> isMatch("aa","aa") → true
> 
> isMatch("aaa","aa") → false
> 
> isMatch("aa", "*") → true
> 
> isMatch("aa", "a*") → true
> 
> isMatch("ab", "?*") → true
> 
> isMatch("aab", "c*a*b") → false

## Solution I with two pointers
```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j, lastI, lastStar = 0, 0, 0, -1
        while i < len(s):
            if j<len(p) and (s[i]==p[j] or p[j]=='?'):
                i += 1
                j += 1
            elif j<len(p) and p[j]=='*':  # match 0 time
                lastI, lastStar = i, j
                j += 1
            elif lastStar != -1:  # backtracking
                j = lastStar+1
                lastI += 1
                i = lastI
            else:
                return False
        while j<len(p) and p[j]=='*':
            j += 1
        return j == len(p)
```

## Solution II with DP (TLE due to )
```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lenS, lenP = len(s)+1, len(p)+1
        cnt = p.count('*')
        if lenP - cnt > lenS:  # trick to get rid of TLE
            return False
        dp = [[False]*lenP for _ in xrange(lenS)]
        dp[0][0] = True
        for i in xrange(1, lenP):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]
        for i in xrange(1, lenS):
            for j in xrange(1, lenP):
                if p[j-1]=='?' or s[i-1]==p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return dp[-1][-1]
```

