class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in xrange(n):
            while 0<nums[i]<=n and nums[i]!=i+1 and nums[i]!=nums[nums[i]-1]:
                # the following line is wrong!!
                # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                t = nums[i]
                nums[i] = nums[t-1]
                nums[t-1] = t
        for i in xrange(n):
            if nums[i] != i+1:
                return i+1
        return n+1

print Solution().firstMissingPositive([1,5,2,4])
