# 56. Merge Intervals

## Problem
- Given a collection of intervals, merge all overlapping intervals.

> For example,
> 
> Given [1,3],[2,6],[8,10],[15,18],
> 
> return [1,6],[8,10],[15,18].

## Solution
```python
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

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
```
