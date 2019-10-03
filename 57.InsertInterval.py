# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        start, end = newInterval.start, newInterval.end
        left, right = [], []
        for i in intervals:
            # 应该先考虑小于的情况
            if start > i.end:  # 目前的区间在待插入区间的右边
                left.append(i)
            elif end < i.start:  # start <= i.end时，有可能是包含，但也有可能带插入区间在目前的左边
                right.append(i)
            else:  # 包含的情况 start <= i.end or end >= i.start
                # start取小，end取大
                start = min(start, i.start)
                end = max(end, i.end)
        return left + [Interval(start, end)] + right
        