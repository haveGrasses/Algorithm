# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        ret = []
        for i in sorted(intervals, key=lambda i: i.start):
            if ret and (i.start <= ret[-1].end):
                ret[-1].end = max(i.end, ret[-1].end)
            else:
                ret.append(i)
        return ret
                