class Solution:
    def canPartition(self, nums):
        total = sum(nums)  # maximal sum
        if total & 1 == 1:  # 奇数显然不行
            return False
        total //= 2  # 某一边的和
        # print(total)
        n = len(nums)
        dp = [[0 for _ in range(total+1)] for _ in range(n+1)]
        # shape of dp: n n+1 rows, total+1 cols
        # print(np.array(dp))
        dp[0][0] = 1  # sum = 0, left and right part sum both to 0
        for i in range(1, n+1):  # fill first col
            dp[i][0] = 1
            
        for i in range(1, total+1):  # fill first row
            dp[0][i] = 0
            
        for i in range(1, n+1):
            for j in range(1, total+1):
                # 注意这三行中的逻辑 当然可以写成一行
                # dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                # 但是判断一下会省区很多无谓计算 比如当j < nums[i-1]的时候，
                # 没必要去看 dp[i-1][j-nums[i-1]]是否为1 因为越界 
                dp[i][j] = dp[i-1][j]
                if j - nums[i-1] >=0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                # dp[i][j]中对应的i实际上是nums[i-1]代表的数字，因此这里是 j-nums[i-1]
                # print(np.array(dp))
        return dp[n][total]
        
