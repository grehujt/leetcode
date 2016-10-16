class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        pre, cur = '', '1'
        for _ in xrange(n-1):
            pre, cur, cnt = cur, '', 1
            for i in xrange(len(pre)):
                if i+1<len(pre) and pre[i]==pre[i+1]:
                    cnt += 1
                else:
                    cur = '%s%d%s' % (cur, cnt, pre[i])
                    cnt = 1
        return cur


print Solution().countAndSay(6)
