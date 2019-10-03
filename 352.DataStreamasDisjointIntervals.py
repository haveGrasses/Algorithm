# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heapq

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
        

    def addNum(self, val: int) -> None:
        if val not in [x[0] for x in self.intervals]:  # avoid same key
        # python3 doesn't allow heap to have the same value key
            heapq.heappush(self.intervals, (val, Interval(val, val)))


    def getIntervals(self):
        mergedIntervals = []
        
        while self.intervals:
            idx, cur = heapq.heappop(self.intervals)
            if not mergedIntervals:  # make a initial add
                mergedIntervals.append((idx, cur))
            else:
                _, prev = mergedIntervals[-1]  # fetch last one to compare
                if prev.end + 1 >= cur.start:
                    prev.end = max(prev.end, cur.end)
                else:
                    mergedIntervals.append((idx, cur))
        self.intervals = mergedIntervals
        return list(map(lambda i: i[1], mergedIntervals))
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
