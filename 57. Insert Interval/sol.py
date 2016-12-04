import bisect


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ioi = bisect.bisect_left([x.start for x in intervals], newInterval.start)
        ret = []
        for item in intervals[:ioi] + [newInterval] + intervals[ioi:]:
            if ret and item.start <= ret[-1].end:
                ret[-1].end = max(ret[-1].end, item.end)
            else:
                ret.append(item)
        return ret


# intervals = [Interval(0, 2), Interval(1, 3), Interval(4, 5)]
intervals = [Interval(1, 5)]
newInterval = Interval(1, 7)
for item in Solution().insert(intervals, newInterval):
    print item.start, item.end
