class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        trimmedStr = str.strip()
        if len(trimmedStr) == 0:
            return 0
        isNegative, i, result = False, 0, 0
        if trimmedStr[0] == '-':
            isNegative = True
            i = 1
        else:
            i = 1 if trimmedStr[0] == '+' else 0
        while i < len(trimmedStr):
            t = ord(trimmedStr[i]) - ord('0')
            if 0 <= t <= 9:
                result = result * 10 + t
            else:
                break
            i += 1
        result = -result if isNegative else result
        if result >= 2147483647:
            return 2147483647
        elif result <= -2147483648:
            return -2147483648
        else:
            return result
