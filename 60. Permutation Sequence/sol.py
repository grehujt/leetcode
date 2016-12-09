class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def bt(nums, used, idx):
            if self.cnt == k:
                self.tar = ''.join(str(i) for i in nums)
                return
            if idx == n:
                self.cnt += 1
                bt(nums, used, 0)
            for i in range(n):
                if not used[i] and not self.tar:
                    nums[idx] = i+1
                    used[i] = True
                    bt(nums, used, idx+1)
                    used[i] = False
        m = reduce(lambda x,y:x*y, range(1,n+1), 1)
        self.cnt, self.tar = 0, None
        bt([0]*n, [False]*n, 0)
        return self.tar
