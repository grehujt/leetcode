class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        print nums
        result = []
        h, t = 0, len(nums)-1
        while h < t:
            n1, n2 = nums[h], nums[t]
            l, r = h+1, t-1
            while l < r:
                n3, n4 = nums[l], nums[r]
                s = n1+n2+n3+n4
                if s == target:
                    result.append([n1, n3, n4, n2])
                    l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s > target:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                else:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            h += 1
            while h < t and nums[h] == nums[h-1]:
                h += 1
        return result

print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
