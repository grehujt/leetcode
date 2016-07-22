class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        i, j, cnt = 0, 1, len(nums)
        while j < cnt:
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i+1

nums = [1,1,2,2,3,3,3]
x = Solution().removeDuplicates(nums)
print nums[:x]
