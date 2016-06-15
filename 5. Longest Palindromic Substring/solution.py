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

print Solution().longestPalindrome('ccc')
