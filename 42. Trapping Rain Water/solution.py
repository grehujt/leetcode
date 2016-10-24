class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n, ret = len(height), 0
        lh, rh = [0]*n, [0]*n
        for i in xrange(1, n):
            lh[i] = max(lh[i-1], height[i-1])
        for i in xrange(n-2, -1, -1):
            rh[i] = max(rh[i+1], height[i+1])
            minH = min(lh[i], rh[i])
            ret += minH-height[i] if minH>height[i] else 0
        return ret

print Solution().trap([4, 2, 3, 2])
