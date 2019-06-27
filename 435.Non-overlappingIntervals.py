class Solution:
    """ 
    算最少需要去掉多少个区间等价于求最多可以形成多少个互不重叠的区间。
    贪心算法，按照区间结尾的大小排序，先结尾的排在前面，每次选择的时候
    选择结尾最早的 且 和已经选择的上的区间不重合的区间（此区间的结尾大于等于上一个区间的开头）

    选择先结尾的原因就是结尾小 能留给后面更大的选择范围。
    """
    
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
        
