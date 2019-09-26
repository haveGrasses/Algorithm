# Definition for an interval.
from typing import List


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        ret = []
        for i in sorted(intervals, key=lambda i: i.start):
            if ret and (i.start <= ret[-1].end):
                ret[-1].end = max(i.end, ret[-1].end)
            else:
                ret.append(i)
        return ret

for i in Solution().merge([Interval(1, 3), Interval(4, 6), Interval(4, 5), Interval(4, 7)]):
    print(i.start, i.end)


class Solution:
    """ 新版没有Interval class的设定了，解法还是一样的 """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if ret and ret[-1][1] >= i[0]:
                ret[-1][1] = max(ret[-1][1], i[1])
            else:
                ret.append(i)
        return ret
