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


# using partition：16%
# attention: lo和hi的开始位置；partition中i和j的初始位置；while的进入条件；内层while的比较不等式等号在哪里；while的break写在内层while之后；
class Solution:
    def findKthLargest(self, nums, k):
        k = len(nums) - k
        lo, hi = 0, len(nums)-1
        while lo < hi:
            j = self.partition(nums, lo, hi)
            if j > k:
                hi = j - 1
            elif j < k:
                lo = j + 1
            else:
                break
        return nums[k]

    def partition(self, nums, lo, hi):
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        # i, j = lo+1, hi  # 不加优化的写法
        
        swap(nums, lo, lo+(hi-lo)//2)  # 加一步优化 对选择pivot的元素进行优化，选lo+(hi-lo)//2位置的
        i, j = lo+1, hi  # 这一步优化后beats 67.91%
        
        # 一定要写while True，而不是while i < j，原因有二：
        # 1、如果while的条件写在外面，里面没有跳出的限制的话，有可能经过两轮的while之后i会变得大于等于j
        # 2、当i和j相等的时候，还是希望更能够进入循环，why？
        # 当 i 和 j 相等的时候还是要走一遍这个 while 循环，原因是lo需要和j交换位置，
        # 交换位置的前提是必须保证nums[j]是小于等于nums[lo]的，走一遍内层的while能够保证这一
        while True:
            while i < hi and nums[i] <= nums[lo]:
                i += 1
            while j > lo and nums[j] > nums[lo]:
                j -= 1
            if i >= j:
                break
            swap(nums, i, j)
        swap(nums, lo, j)
        return j

