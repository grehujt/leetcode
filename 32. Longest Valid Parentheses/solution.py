class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxCnt = 0
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append((i, 'l'))
            else:
                if not stack or stack[-1][1] == 'r':
                    stack.append((i, 'r'))
                else:
                    stack.pop()
                    maxCnt = max(maxCnt, i+1 if not stack else i-stack[-1][0])
        return maxCnt

print Solution().longestValidParentheses('((()))()')
