class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        for i in xrange(1, n):
            dp[i] = min(dp[j] for j in xrange(i) if j+nums[j]>=i) + 1
        return dp[-1]


print Solution().jump([0])
