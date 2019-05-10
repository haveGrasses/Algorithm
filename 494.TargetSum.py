class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        limit = sum(nums)
        if abs(S) > limit:
            return 0
        dp = [0] * (2*limit+1)
        dp[0+limit] = 1
        for i in range(len(nums)):
            update = [0] * (2*limit+1)
            for j in range(-1*limit, limit+1):
                if dp[j] > 0:
                    update[j+nums[i]] += dp[j]
                    update[j-nums[i]] += dp[j]
            dp = update
        return dp[limit+S]
  
# add dfs method: a slower but acceptable way

# 用next的方法是对二维dp空间的一个简化 如果还是用二维的dp，将不需要用next
# 原因还不知道
