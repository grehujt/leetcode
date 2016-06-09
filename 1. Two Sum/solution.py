class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n1 in enumerate(nums):
            n2 = target - n1
            if n2 in d:
                return [i, d[n2]]
            else:
                d[n1] = i
