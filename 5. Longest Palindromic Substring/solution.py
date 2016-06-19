class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        newS = '#%s#' % '#'.join(s)
        length, center, rightMost, maxCenter, maxLen, i = len(newS), 0, 0, 0, 0, 0
        pArr = [0] * length
        while i < length:
            pArr[i] = 1 if rightMost < i else min(rightMost-i, pArr[(center << 1) - i])
            while i + pArr[i] < length and i - pArr[i] > -1 and newS[i + pArr[i]] == newS[i - pArr[i]]:
                pArr[i] += 1
            if i + pArr[i] > rightMost:
                center = i
                rightMost = i + pArr[i]
                if pArr[i] > maxLen:
                    maxLen = pArr[i]
                    maxCenter = i
            i += 1
        start = (maxCenter - maxLen + 1) >> 1
        return s[start: start + maxLen - 1]

print Solution().longestPalindrome('cacc')
