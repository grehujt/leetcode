# 10. Regular Expression Matching

### Problem
- Implement regular expression matching with support for '.' and '*'.
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.
- The matching should cover the entire input string (not partial).
- The function prototype should be:

```c
bool isMatch(const char *s, const char *p)
```

- Some examples:

```c
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
```


### Solution

1. Recursion: (TLE..)

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def _match(s, p, si, pi):
            # base case, if both si and pi reach tail, matched
            if si==len(s) and pi==len(p): return True
            # handle '*'
            if pi+1<len(p) and p[pi+1] == '*':
                # '#' can match nothing
                # or more than once
                return _match(s, p, si, pi+2) or ((si<len(s) and (s[si]==p[pi] or p[pi]=='.')) and _match(s, p, si+1, pi))
            else:  # non '*' case
                # match char by char
                return (si<len(s) and pi<len(p) and (s[si]==p[pi] or p[pi]=='.')) and _match(s, p, si+1, pi+1)
        return _match(s, p, 0, 0)
```

**Time complexity analysis:**
- Worst case:
> Worst cases happen when '\*' occurs in all the odd positions, e.g. 'q\*w\*c\*...'. And in these case, we split the original problem into 2 sub-problem, _match(s, p, si, pi+2) and _match(s, p, si+1, pi)), so **T(n) = 2T(n-1) + 1, which results in O(2^n)**. 
- Best case:
> Likewise, best cases happen when no '\*' occurs. In this case, __T(n) = T(n-1) + 1, which results in O(n)__.

2. Dynamic programming:

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lenS, lenP = len(s), len(p)
        # dp[i][j]==True means s[:i] matches p[:j]
        dp = [[False]*(lenP+1) for i in xrange(lenS+1)]
        dp[0][0] = True
        for si in xrange(lenS+1):  # starting from 0, which inits the dp[0][:]
            for pi in xrange(1, lenP+1):  # starting from 1
                if p[pi-1] != '*':
                    dp[si][pi] = si>0 and dp[si-1][pi-1] and (s[si-1]==p[pi-1] or p[pi-1]=='.')
                else:  # handle '*'
                    if dp[si][pi-1] or dp[si][pi-2]:
                        # matches zero time or once
                        dp[si][pi] = True
                    else:
                        # matches more than once
                        dp[si][pi] = si>0 and dp[si-1][pi] and (s[si-1]==p[pi-2] or p[pi-2]=='.')
        return dp[lenS][lenP]
```

**Time complexity analysis: Clearly O(n^2)**