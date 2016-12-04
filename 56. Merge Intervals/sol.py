
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
        ret = []
        for item in sorted(intervals, key=operator.attrgetter('start')):
            if ret and ret[-1].end >= item.start:
                ret[-1].end = max(ret[-1].end, item.end)
            else:
                ret += item,
        return ret


a = Interval(0, 3)
b = Interval(-1, 2)
for item in Solution().merge([a, b]):
    print item.start, item.end
