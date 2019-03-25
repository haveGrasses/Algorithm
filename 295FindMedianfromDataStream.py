from heapq import *


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.samll, self.large = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # use negative value in samll to keep big value in the front 
        # caz we need to fetch the first one in samll to calc the median value 
        # (because it is a data stream, we can onluy access its first value not its last one, the size is changing)
        # and the first one must be the biggest one in samll, so use negative value to keep big one ahead in a heap
        
        heappush(self.samll, -heappushpop(self.large, num))  # add new num to large, pop the samllest one in large to samll
        if len(self.large) < len(self.samll):  # keep the size of large always equal or only one bigger than samll
            heappush(self.large, -heappop(self.samll))

    def findMedian(self):
        """
        :rtype: float
        """
        # samll, large = self.heaps
        if len(self.large) > len(self.samll):
            return self.large[0]
        return (self.large[0] - self.samll[0]) / 2  # pay attention to the minus, nums in samll is kept negative
