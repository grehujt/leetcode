class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 2147483647
        isNeg = (dividend<0 and divisor>0) or (dividend>0 and divisor<0)
        dd, dr, res = abs(dividend), abs(divisor), 0
        while dr <= dd:
            tmp, i = dr, 1
            while tmp <= dd:
                tmp <<= 1
                i += 1
            res += 1 << (i-2)
            dd -= dr << (i-2)
        return -res if isNeg else res
