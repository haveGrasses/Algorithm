class Solution:
    """ a binary search method """
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if nums[mid] > nums[hi]:  # left part is in order, the pivot value should be in the right part
                lo = mid + 1
            elif nums[mid] < nums[hi]:  # the right part is in order, pivot is in the left part
                hi = mid   # todo: not mid-1, why: nums[mid] may be the pivot value
            else:  # nums[mid] == nums[hi] == nums[lo]
                # the following three line can be deleted, but it ensures the right index of pivot value
                if nums[hi-1] > nums[hi]:  # pivot encountered
                    lo = hi  # pivot
                    break  # 注1
                hi -= 1  # When num[mid] == num[hi], we couldn't sure the position of minimum in mid's left or right, so just let upper bound reduce one.
        return nums[lo]


print(Solution().findMin([1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1]))
# eg
# 2,2,2,0,1,2: nums[mid] = 2, nums[lo] = 2, mums[hi] = 2, minimal = 0, right to mid
# 2,0,1,2,2,2,2: nums[mid] = 2, nums[lo] = 2, mums[hi] = 2, minimal = 1, left to mid
# so when num[mid] == num[hi], we couldn't sure the position of minimum in mid's left or right

# 注1：和else里面三行一样的功能
# if nums[hi-1] <= nums[hi]:  #  和上面三行一样的效果
#     lo = hi - 1  # pivot
#     break