class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j, n = 0, 0, len(nums)
        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

nums = [4,1,3,3,3,2,3]
x = Solution().removeElement(nums,3)
print nums[:x]
