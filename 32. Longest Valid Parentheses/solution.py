class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        cnt = 0
        maxCnt = 0
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                    cnt += 2
                else:
                    cnt = 0
                    stack = []
                maxCnt = max(maxCnt, cnt)
        return maxCnt

print Solution().longestValidParentheses('((())')

