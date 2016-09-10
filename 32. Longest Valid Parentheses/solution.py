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
            if s[i-1] == '(':
                dp[i] = 0
            else:
                j = i-2-dp[i-1]
                dp[i] = dp[i-1]+dp[j]+2 if j>=0 and s[j]=='(' else 0
                maxCnt = max(maxCnt, dp[i])
        return maxCnt

print Solution().longestValidParentheses('((()))()')
