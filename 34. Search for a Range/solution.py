class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def _binary_search(beg, end, t):
            while beg < end:
                mid = beg + ((end-beg) >> 1)
                if nums[mid] < t:
                    beg = mid+1
                else:
                    end = mid
            return beg

        idx = _binary_search(0, len(nums), target)
        if idx==len(nums) or nums[idx]!=target:
            return [-1, -1]
        else:
            return [idx, _binary_search(idx+1, len(nums), target+1) - 1]

print Solution().searchRange([1,2,2,3], 2)
