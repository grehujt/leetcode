class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dq = collections.deque()
        charSet = set()
        maxLen = 0
        for c in s:
            if c in charSet:
                while True:
                    leftMostChar = dq.popleft()
                    charSet.remove(leftMostChar)
                    if leftMostChar == c:
                        break
            charSet.add(c)
            dq.append(c)
            maxLen = len(dq) if maxLen < len(dq) else maxLen
        return maxLen
