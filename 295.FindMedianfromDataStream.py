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
        # (because it is a data stream, we can only access its first value not its last one, the size is changing)
        # and the first one must be the biggest one in samll, so use negative value to keep big one ahead in a heap
        
        heappush(self.samll, -heappushpop(self.large, num))
        # add new num to large, pop the samllest one in large to samll
        if len(self.large) < len(self.samll):  # keep the size of large always equal or only one bigger than samll
            heappush(self.large, -heappop(self.samll))

    def findMedian(self):
        """
        :rtype: float
        """
        # samll, large = self.heaps
        if len(self.large) > len(self.samll):
            return self.large[0]
        return (self.large[0] - self.samll[0]) / 2
        # pay attention to the minus, nums in samll is kept negative from its original values

 
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []  

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        samll, large = self.heaps  # when small and large change, heaps changes accordingly, because list is changable?
        heappush(samll, -heappushpop(large, num))
        if len(large) < len(samll):
            heappush(large, -heappop(samll))

    def findMedian(self):
        """
        :rtype: float
        """
        samll, large = self.heaps
        if len(large) > len(samll):
            return large[0]
        return (large[0] - samll[0]) / 2

    
# the above methods is suitable for `data stream`, but for a given array, 
# the most efficient way is to use `PARTITION`, no extra space and O(logn)? i guess

# TODO
def findMedian(arr):
    # 见 215
    pass


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
