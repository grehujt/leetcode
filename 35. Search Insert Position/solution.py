class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def _search(lo, hi):
            while lo <= hi:
                mid = lo + ((hi-lo) >> 1)
                if nums[mid] < target:
                    lo = mid+1
                else:
                    hi = mid-1
            return lo
        return _search(0, len(nums)-1)

print Solution().searchInsert([1,2,3],4)
