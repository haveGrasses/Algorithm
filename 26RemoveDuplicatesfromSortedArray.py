class Solution:
    """ idx 所指的位置是上一个unique的数，每次发现unique的数需要在idx+1的位置插入"""
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                idx += 1
                nums[idx] = nums[i]
        return idx+1


class Solution:
    """ idx 所指的位置是下一个unique的数，每次发现unique的数需要在idx的位置插入 """
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                idx += 1
        return idx
