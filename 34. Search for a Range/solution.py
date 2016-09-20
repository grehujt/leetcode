import bisect


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = bisect.bisect_left(nums, target)
        if lo==len(nums) or nums[lo]!=target:
            return [-1, -1]
        else:
            return [lo, bisect.bisect(nums, target, lo=lo+1)-1]

print Solution().searchRange([1,2,2,3], 2)
