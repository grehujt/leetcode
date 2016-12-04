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
        if len(intervals) == 0:
            return [newInterval]
        ioi = bisect.bisect_left([x.start for x in intervals], newInterval.start)
        tmp = intervals[:ioi] + [newInterval] + intervals[ioi:]
        ret = [tmp[0]]
        for i in range(1, len(tmp)):
            item1 = ret[-1]
            item2 = tmp[i]
            if item2.start <= item1.end:
                item1.end = max(item1.end, item2.end)
            else:
                ret.append(item2)
        return ret


# intervals = [Interval(0, 2), Interval(1, 3), Interval(4, 5)]
intervals = [Interval(1, 5)]
newInterval = Interval(1, 7)
for item in Solution().insert(intervals, newInterval):
    print item.start, item.end
