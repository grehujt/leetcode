class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        keys = sorted(nums)
        for i in xrange(len(keys) - 2):
            if i != 0 and keys[i] == keys[i-1]:  # remove dup
                continue
            n1 = keys[i]
            j, k = i + 1, len(keys) - 1
            while j < k:
                n2, n3 = keys[j], keys[k]
                s = n1 + n2 + n3
                if s == 0:
                    result.append([n1, n2, n3])
                    j += 1
                    k -= 1
                    while j < k and keys[j] == keys[j-1]:  # remove dup
                        j += 1
                    while j < k and keys[k] == keys[k+1]:  # remove dup
                        k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return result
