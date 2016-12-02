
import operator
# import collections

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 1:
            return []
        sortedIntervals = sorted(intervals, key=operator.attrgetter('start'))
        ret = [sortedIntervals[0]]
        for i in range(1, len(sortedIntervals)):
            item1 = ret[-1]
            item2 = sortedIntervals[i]
            if item1.end >= item2.start:
                item1.end = max(item1.end, item2.end)
            else:
                ret.append(item2)
        return ret


a = Interval(0, 3)
b = Interval(-1, 2)
for item in Solution().merge([a , b]):
    print item.start, item.end
