class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = None
        for i in xrange(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                left = i-1
                break
        if left is not None:
            beg, end = left+1, len(nums)-1
            while beg+1 < end:
                mid = (beg+end) >> 1
                if nums[mid] > nums[left]:
                    beg = mid
                else:
                    end = mid
            if nums[end] > nums[left]:
                nums[end], nums[left] = nums[left], nums[end]
            else:
                nums[beg], nums[left] = nums[left], nums[beg]

            left += 1
            right = len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        else:
            nums.sort()
        # print nums

Solution().nextPermutation([5,4,7,5,3,2])
