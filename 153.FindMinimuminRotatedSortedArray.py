class Solution(object):
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            if nums[lo] < nums[hi]:  # 数组天然有序
                return nums[lo]
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[lo]:
                hi = mid
            elif nums[mid] > nums[lo]:
                lo = mid
            else:
                break
        return nums[hi]

    # 不要看上面的代码了...
    # 这是一个更简洁的实现：
    # 第一个方法之所以冗长是因为是在拿mid和lo比较，mid是有可能等于lo的，所以最后多了个else break的情况，并且不能处理数据天然有序的情况。。
    # 而下面这个方法是在拿mid和hi比，mid永远是小于hi的，所以不会出现不break就会死循环的情况
    def findMin2(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[hi]


print(Solution().findMin([3,4,5,1,2]))
