class Solution:
    """ 记录下一个不为0的元素插入的位置即可，剩下的位置填0
    这种用指针记录下一个插入位置的方法类似于26 RemoveDuplicatesfromSortedArray
    """
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos] = nums[i]
                non_zero_pos += 1
        while non_zero_pos < len(nums):
            nums[non_zero_pos] = 0
            non_zero_pos += 1
