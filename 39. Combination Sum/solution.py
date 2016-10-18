class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def bt(beg, t, tmp):
            if t == 0:
                result.append([x for x in tmp])
            else:
                for i in xrange(beg, len(candidates)):
                    d = candidates[i]
                    tmp.append(d)
                    if t-d < 0:
                        tmp.pop()
                        return
                    else:
                        bt(i, t-d, tmp)
                        tmp.pop()

        result = []
        candidates.sort()
        bt(0, target, [])
        return result

print Solution().combinationSum([2,3,6,7], 7)
