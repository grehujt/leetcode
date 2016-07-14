class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        keys = nums
        for i in xrange(len(keys) - 2):
            if i != 0 and keys[i] == keys[i-1]:
                continue
            n1 = keys[i]
            if n1 * 3 > 0:
                break
            j, k = i + 1, len(keys) - 1
            while j < k:
                n2, n3 = keys[j], keys[k]
                if n3 * 3 < 0:
                    break
                s = n1 + n2 + n3
                if s == 0:
                    result.append([n1, n2, n3])
                    j += 1
                    k -= 1
                    while j < k and keys[j] == keys[j-1]:
                        j += 1
                    while j < k and keys[k] == keys[k+1]:
                        k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return result
