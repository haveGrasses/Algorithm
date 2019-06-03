# 求第k *大* 要用 最 *小* 堆，才能拿到前k大的元素里面最小的那个，就是第k大
# 所以关键就是怎么维护这个堆，先装k个到堆里，之后每次来一个值，让它去更新目前堆中的最小值，保留较大的进堆

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

    
# 下面这个方法充分说明第一个方法简直弱智
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k:  # 严格大于，实际维护的heap的大小是k个，但是过程中先是让heap里的元素多一个，然后pop掉最小的那一个，
                # 这样就能保证每次的pop不会出现下面的问题：
                # 如果一直维持k个长度不变的情况下，来一个就pop最小的出去，有可能这一次pop的元素实际上比下一次push的元素大
                # 但是如果长度是k+1的话，这一次pop的元素如果比下一次add的大的话，是不会影响第k大的
                heapq.heappop(heap)
            # 当heap中非元素个数大于k个之后会重复进行添加删除添加删除的操作，最终以删除结束，一次次过滤掉小的元素
        return heapq.heappop(heap)
