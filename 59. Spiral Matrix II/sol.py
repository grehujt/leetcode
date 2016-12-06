class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num = 1
        ret = [[0]*n for _ in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1
        while 1:
            for i in range(left, right+1):
                ret[top][i] = num
                num += 1
            top += 1
            if top > bottom: break
            for i in range(top, bottom+1):
                ret[i][right] = num
                num += 1
            right -= 1
            if left > right: break
            for i in range(right, left-1, -1):
                ret[bottom][i] = num
                num += 1
            bottom -= 1
            if top > bottom: break
            for i in range(bottom, top-1, -1):
                ret[i][left] = num
                num += 1
            left += 1
            if left > bottom: break
        return ret

print Solution().generateMatrix(3)
