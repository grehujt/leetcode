class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def _search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = lo + ((hi-lo) >> 1)
                l, h = _search(lo, mid), _search(mid+1, hi)
                return max(l, h) if -1 in l+h else [l[0], h[1]]
            return [-1, -1]
        return _search(0, len(nums)-1)

print Solution().searchRange([1,2,2,3], 2)
