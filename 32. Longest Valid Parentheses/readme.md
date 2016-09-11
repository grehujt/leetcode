# 32. Longest Valid Parentheses

## Problem
- Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
- For "(()", the longest valid parentheses substring is "()", which has length = 2.
- Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

##Solution using DP
```python
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        maxCnt = 0
        dp = [0] * (size+1)
        for i in xrange(1, size+1):
            if s[i-1] == ')':
                j = i-2-dp[i-1]
                dp[i] = dp[i-1]+dp[j]+2 if j>=0 and s[j]=='(' else 0
                maxCnt = max(maxCnt, dp[i])
        return maxCnt
```

**Key points:**
- dp[i] stands for the length of longest valid parentheses count through s[:i]
- if s[i-1] == '(', dp[i] is 0 clearly
- if s[i-1] == ')', dp[i] might come from 2 parts, (e.g. "()(())", one is "()", the other is ending "(())"). Denote j = i-1 - dp[i-1] - 1, s[j] should be next to the first character of dp[i-1] pointing at if j is valid (j>=0 and s[j]=='('), otherwise dp[i] = 0.

## Solution using Stack
```python
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxCnt = 0
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append((i, 'l'))
            else:
                if not stack or stack[-1][1] == 'r':
                    stack.append((i, 'r'))
                else:
                    stack.pop()
                    maxCnt = max(maxCnt, i+1 if not stack else i-stack[-1][0])
        return maxCnt
```

**Key points:**
- We need to store the location as well as the type (left or right parenthesis) to calculate the length.
