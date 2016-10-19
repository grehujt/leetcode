class Solution(object):
    def combinationSum2(self, candidates, target):
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
                    if i!=beg and d==candidates[i-1]:
                        continue
                    tmp.append(d)
                    if t-d < 0:
                        tmp.pop()
                        return
                    else:
                        bt(i+1, t-d, tmp)
                        tmp.pop()

        result = []
        candidates.sort()
        bt(0, target, [])
        return result

print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
