class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lenS, lenP = len(s), len(p)
        dp = [[False]*(lenP+1) for i in xrange(lenS+1)]
        dp[0][0] = True
        for si in xrange(lenS+1):
            for pi in xrange(1, lenP+1):
                if p[pi-1] != '*':
                    dp[si][pi] = si>0 and dp[si-1][pi-1] and (s[si-1]==p[pi-1] or p[pi-1]=='.')
                else:
                    if dp[si][pi-1] or dp[si][pi-2]:
                        dp[si][pi] = True
                    else:
                        dp[si][pi] = si>0 and dp[si-1][pi] and (s[si-1]==p[pi-2] or p[pi-2]=='.')
        return dp[lenS][lenP]

print Solution().isMatch('aa','c*a*')