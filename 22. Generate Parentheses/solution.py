class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def fill(result, s, l, r):
            if l == 0 and r == 0:
                result.append(s)
                return
            if l:
                fill(result, s+'(', l-1, r+1)
            if r:
                fill(result, s+')', l, r-1)
        result = []
        fill(result, '', n, 0)
        return result

print Solution().generateParenthesis(3)
