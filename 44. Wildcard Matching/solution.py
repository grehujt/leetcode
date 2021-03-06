class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lenS, lenP = len(s)+1, len(p)+1
        cnt = p.count('*')
        if lenP - cnt > lenS:
            return False
        dp = [[False]*lenP for _ in xrange(lenS)]
        dp[0][0] = True
        for i in xrange(lenS):
            for j in xrange(1, lenP):
                if p[j-1]=='?' or (i>0 and s[i-1]==p[j-1]):
                    dp[i][j] = dp[i-1][j-1]  # will cause probem in other lang which -1 index is not supported
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or (i>0 and dp[i-1][j])
        return dp[-1][-1]

print Solution().isMatch('a', '?')
