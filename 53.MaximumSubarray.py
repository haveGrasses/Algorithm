class Solution:
    """ genius solution, using dp(?)
    对于每一个数来说，其有可能有两个选择，一个是作为已累积字串的结尾，
    另一个是作为新字串的开头
    只有当前面已累计的和是正数时，
    后一个数累积到前面的字串中才会大于该数作为一个新字串的开头得到的结果
    因此程序执行后的nums的每一元素代表这个位置能取得的连续字串的最大和
    """
    def maxSubArray1(self, nums: List[int]) -> int:
        """ emmmm，不太喜欢这个解法了 """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

    def maxSubArray2(self, nums: List[int]) -> int:
        """ 正规dp方法 """
        dp = [nums[0] for _ in range(len(nums))]
        maxSum = dp[0]
        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i]
            maxSum = max(dp[i], maxSum)
        return maxSum

    def maxSubArray(self, nums: List[int]) -> int:
        """ 第一种方法 """
        maxSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
                maxSum = max(maxSum, nums[i])
        return maxSum
