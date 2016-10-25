class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret, s = 0, []
        for i, h in enumerate(height):
            while s and height[s[-1]]<=h:
                j = s.pop()
                ret += (min(h, height[s[0]])-height[j])*(j-s[-1]) if s else 0
            s.append(i)
        return ret

print Solution().trap([4, 2, 3, 2])
