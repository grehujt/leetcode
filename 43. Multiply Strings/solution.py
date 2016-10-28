class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1, len2 = len(num1), len(num2)
        arr = [0] * (len1+len2)
        for i in xrange(len1-1, -1, -1):
            for j in xrange(len2-1, -1, -1):
                arr[i+j+1] += int(num1[i]) * int(num2[j])
        for i in xrange(len1+len2-1, 0, -1):
            if arr[i] > 9:
                arr[i-1] += arr[i] / 10
                arr[i] %= 10
        ret = ''.join(str(i) for i in arr).lstrip('0')
        return ret if ret else '0'

print Solution().multiply('0','0')


