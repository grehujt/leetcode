class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastOccur = {}
        j, maxLen = 0, 0
        for i, c in enumerate(s):
            if c in lastOccur:
                j = max(j, lastOccur[c] + 1)
            lastOccur[c] = i
            maxLen = max(maxLen, i - j + 1)
        return maxLen
