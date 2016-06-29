class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2: return 0
        l, r, largest = 0, len(height)-1, -1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            largest = max(area, largest)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return largest