from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = deque()  # save possible candidates
        res = []
        for i, v in enumerate(nums):
            # ensure d's order, index increasing, corresponding value decreasing
            while d and nums[d[-1]] < v:
                d.pop()  # pop right
            d += i,  # same as d += [i] but more elegant

            if d[0] == i-k:
                d.popleft()
            if i >= k-1:
                res += nums[d[0]],
        return res
        
