class Solution:
    
    def sortIntervals(self, intervals):
        return sorted(intervals, key=lambda x: x[1])
        
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = self.sortIntervals(intervals)
        res = 1
        pre = intervals[0]
        for i in intervals[1:]:
            if i[0] >= pre[1]:
                res += 1
                pre = i
        return len(intervals) - res
        
