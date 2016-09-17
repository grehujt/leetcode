class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beg, end = 0, len(nums)-1
        while beg <= end:
            mid = (beg+end) >> 1
            if nums[mid] == target:
                return mid
            if nums[beg] <= nums[mid]:
                if nums[beg] <= target < nums[mid]:
                    end = mid-1
                else:
                    beg = mid+1
            else:
                if nums[mid] < target <= nums[end]:
                    beg = mid+1
                else:
                    end = mid-1
        return -1


print Solution().search([1,3],1)
