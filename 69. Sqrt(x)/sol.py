class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = x
        while ret*ret > x:
            ret = (ret + x/ret) >> 1
        return ret


print Solution().mySqrt(0)
