class Solution:
	""" genius solution, using dp(?)
	对于每一个数来说，其有可能有两个选择，一个是作为已累积字串的结尾，
	另一个是作为新字串的开头
	只有当前面已累计的和是正数时，
	后一个数累积到前面的字串中才会大于该数作为一个新字串的开头得到的结果
	因此程序执行后的nums的每一元素代表这个位置能取得的连续字串的最大和
	"""
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
                