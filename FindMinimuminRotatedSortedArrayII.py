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
                if nums[hi-1] < nums[hi]:  # pivot encountered
                    lo = hi-1  # pivot
                    break
                hi -= 1
        return nums[lo]
