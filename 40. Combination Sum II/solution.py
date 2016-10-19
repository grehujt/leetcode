class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def bt(beg, t, tmp, solSet):
            if t == 0:
                sol = ''.join(str(x) for x in tmp)
                if sol not in solSet:
                    solSet.add(sol)
                    result.append([x for x in tmp])
            else:
                for i in xrange(beg, len(candidates)):
                    d = candidates[i]
                    tmp.append(d)
                    if t-d < 0:
                        tmp.pop()
                        return
                    else:
                        bt(i+1, t-d, tmp, solSet)
                        tmp.pop()

        result = []
        candidates.sort()
        bt(0, target, [], set())
        return result

print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
