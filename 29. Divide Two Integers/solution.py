class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 2147483647
        if divisor == 1 or divisor == -1:
            if dividend == -2147483648:
                return 2147483647 if divisor == -1 else -2147483648
            return -dividend if divisor == -1 else dividend
        if divisor == -2147483648:
            return 1 if dividend == -2147483648 else 0

        isNeg = (dividend<0 and divisor>0) or (dividend>0 and divisor<0)
        dd, dr, res = abs(dividend), abs(divisor), 0
        dividend += dr if dividend == -2147483648 else 0
        while dr <= dd:
            tmp, i = dr, 1
            while tmp <= dd:
                tmp <<= 1
                i += 1
            res += (1 << (i-2))
            dd -= (dr << (i-2))
        return -res if isNeg else res
