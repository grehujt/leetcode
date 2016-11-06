import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def bt(ret, tmpArr, used, n):
            if n == len(nums):
                ret.append(copy.copy(tmpArr))
                return
            for i, x in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    tmpArr[n] = x
                    bt(ret, tmpArr, used, n+1)
                    used[i] = False
        ret, n = [], len(nums)
        bt(ret, [0]*n, [False]*n, 0)
        return ret

print Solution().permute([1,2,3])
