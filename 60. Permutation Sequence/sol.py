class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        facs = [1] * (n+1)
        for i in range(2, n+1):
            facs[i] = i * facs[i-1]
        nums = range(1, n+1)
        ret, k = [], k-1
        for i in range(1, n+1):
            idx = k / facs[n-i]
            ret.append(nums.pop(idx))
            k -= idx * facs[n-i]
        return ''.join(str(i) for i in ret)


print Solution().getPermutation(3, 5)
