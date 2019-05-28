class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1  # 定义初始条件的时候需要定义到多大的长度？
        for i in range(2, n+1):
            # 对每一个i，遍历比它小的取值j 对i进行分割 对于每一个i 可以选择上一轮循环的j得到的结果
            # 也可以选择按这一轮的j进行分割 对于这一轮的j 可以选择对i-j继续分割 可以就保持j 
            # 相当于仅仅将i分成j和i-j两部分 对应额乘积是i*（i-j），
            # 而如果要对i-j继续分割 由于i-j一定是小于i的 因此i-j的最优分割乘积已经知道了 
            # 对应的i的分割乘积为i*dp[i-j]
            for j in range(1, i):
                dp[i] = max([j*dp[i-j], j*(i-j), dp[i]])
                
        return dp[n]
