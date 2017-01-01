class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        beg, end = 0, x
        while beg+1 < end:
            mid = (beg+end) >> 1
            if mid*mid == x: return mid
            beg, end = (beg, mid) if mid*mid > x else (mid, end)
        return end if end*end <= x else beg

print Solution().mySqrt(10)
