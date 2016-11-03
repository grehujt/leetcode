class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, reached, maxR, ret = len(nums), 0, 0, 0
        for i in xrange(n):
            if i > reached:
                if maxR >= n-1: return ret+1
                reached = maxR
                ret += 1
            maxR = max(maxR, i+nums[i])
        return ret


print Solution().jump([0])
