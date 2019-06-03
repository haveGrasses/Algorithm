import heapq
class Solution:
    def findKthLargest(self, nums, k):
        res = []
        for i in nums:
            if len(res) < k:
                heapq.heappush(res, i)
            else:
                minimal = heapq.heappop(res)
                if minimal < i:
                    heapq.heappush(res, i)
                else:
                    heapq.heappush(res, minimal)
        return heapq.heappop(res)
