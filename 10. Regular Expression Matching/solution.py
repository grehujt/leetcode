class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lenS, lenP = len(s)+1, len(p)+1
        #cnt = p.count('*') << 1  # trick from problem 44, not useful
        #if lenP - cnt > lenS:
        #    return False
        dp = [[False]*lenP for _ in xrange(lenS)]
        dp[0][0] = True
        for si in xrange(lenS):
            for pi in xrange(1, lenP):
                if p[pi-1] != '*':
                    dp[si][pi] = si>0 and dp[si-1][pi-1] and (s[si-1]==p[pi-1] or p[pi-1]=='.')
                else:
                    dp[si][pi] = dp[si][pi-2] or (si>0 and dp[si-1][pi] and (s[si-1]==p[pi-2] or p[pi-2]=='.'))
        return dp[-1][-1]

print Solution().isMatch('aa','c*a*')
