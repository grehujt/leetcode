class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        maxCnt = 0
        dp = [[False]*size for _ in xrange(size)]
        for i in xrange(size-2, -1, -1):
            for j in xrange(size-1, i, -1):
                if j-i == 1:
                    if s[i]=='(' and s[j]==')':
                        dp[i][j] = True
                        maxCnt = max(maxCnt, 2)
                else:
                    if (s[i]=='(' and s[j]==')' and dp[i+1][j-1]) or \
                    (s[i] == '(' and s[i+1]==')' and dp[i+2][j]) or \
                    (s[j-1]=='(' and s[j]==')' and dp[i][j-2]):
                        dp[i][j] = True
                        maxCnt = max(maxCnt, j-i+1)
        return maxCnt

print Solution().longestValidParentheses('((()))()')  #problem test case!

