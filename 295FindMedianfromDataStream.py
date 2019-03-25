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
        # samll, large = self.heaps
        heappush(self.samll, -heappushpop(self.large, num))
        if len(self.large) < len(self.samll):
            heappush(self.large, -heappop(self.samll))

    def findMedian(self):
        """
        :rtype: float
        """
        # samll, large = self.heaps
        if len(self.large) > len(self.samll):
            return self.large[0]
        return (self.large[0] - self.samll[0]) / 2
