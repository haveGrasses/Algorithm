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
    
    def canPartition(self, nums):
        """ optimization of space 
        每次循环用到的只是上一次更新的dp的值，所以不需要再存二维矩阵,直接在上一次的基础上更新 
        """
        total = sum(nums)
        if total & 1 == 1:
            return 0
        
        total //= 2
        
        dp = [0 for _ in range(total+1)] 
        dp[0] = 1  # 无论i为多少，一定能构成和0
        
        for n in nums:
            for j in range(total, 0, -1):  # 注意是要从后往前进行更新！！！
                # why: 加入目前给定上一个num更新出来的dp，现在要在这个dp上进行更新
                # 如果从left往right方向更新，则上一轮left part的那些值已经被这一轮的
                # 更新覆盖掉了，所以如果从right往left更新的话就不会影响
                # 更新下一个值需要用到的left part的东西
                if j >= n:  # 本次循环直接在上一次循环的dp上进行更改
                    dp[j] = dp[j] or dp[j-n]
        return dp[-1]  # return dp[total]
    # todo: use memo to avoid repeat calculations
        
