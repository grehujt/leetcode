class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2: return 0
        l, r, largest = 0, len(height)-1, -1
        while l < r:
            heightL, heightR = height[l], height[r]
            area = min(heightL, heightR) * (r - l)
            largest = max(area, largest)
            if heightL < heightR:
                l += 1
                while height[l] < heightL:
                    l += 1
            else:
                r -= 1
                while height[r] < heightR:
                    r -= 1
        return largest