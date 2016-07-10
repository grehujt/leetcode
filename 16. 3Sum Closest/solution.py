import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        minDiff, minS = sys.maxint, None
        nums.sort()
        keys = nums
        for i in xrange(len(keys) - 2):
            if i != 0 and keys[i] == keys[i-1]:
                continue
            n1 = keys[i]
            j, k = i + 1, len(keys) - 1
            while j < k:
                n2, n3 = keys[j], keys[k]
                s = n1 + n2 + n3
                d = abs(s - target)
                if d == 0:
                    return s
                if minDiff > d:
                    minDiff = d
                    minS = s
                if s < target:
                    j += 1
                    while j < k and keys[j] == keys[j-1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and keys[k] == keys[k+1]:
                        k -= 1
        return minS

print Solution().threeSumClosest([1,2,4,8,16,32,64,128], 82)
