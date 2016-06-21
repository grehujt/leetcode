# 8. String to Integer (atoi)

### Problem
- Implement atoi to convert a string to an integer.
- The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
- Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
- The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
- If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
- If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

### Solution

```python
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0: return 0
        isNegative, i, result = False, 0, 0
        while i < len(str) and str[i] == ' ': i += 1
        if len(str) == i: return 0
        isNegative = str[i]=='-'
        i += 1 if str[i]=='-' or str[i]=='+' else 0
        cnt = 0
        while i < len(str) and cnt <= 10:
            t = ord(str[i]) - ord('0')
            if 0 <= t <= 9:
                result = result * 10 + t
            else:
                break
            i += 1
            cnt += 1
        result = -result if isNegative else result
        if result >= 2147483647:
            return 2147483647
        elif result <= -2147483648:
            return -2147483648
        else:
            return result
```

