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
