class Solution:
    def nextPermutation(self, nums) -> None:
        """
        half bms, 题意就是找到离nums最近的比它大的数（最小的最大数），
        做法是从尾部向前扫，找到第一个非递增的位置i，题目就等同于找到从i位置开始到最后这段数字离它最近比位置i大的数
        两者交换位置，之后由于nums[i+1:]是递减序列，反序变成递增序列即可
        需要注意的点：
            1. 如果nums一直是降序的，说明没有第一个非递增的位置i，此时直接反序即可，这两种情况共享的操作是反序
            2. 找比位置i大的最小的数的时候，如果有多个，需要取靠后的那个（因为需要保持降序），因此nums[i] - nums[index] <= delta中有个等号
        """
        index = len(nums) - 1
        while index > 0 and nums[index] <= nums[index - 1]:
            index -= 1
        index -= 1
        if index != -1:
            pos = None
            delta = float('inf')
            for i in range(index, len(nums)):
                if 0 < nums[i] - nums[index] <= delta:
                    delta = nums[i] - nums[index]
                    pos = i
            nums[index], nums[pos] = nums[pos], nums[index]

        start, end = index + 1, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


nums = [2,3,1,3,3]
Solution().nextPermutation(nums)
print(nums)  # [2,3,3,1,3]
