class Solution:
    def numDecodings(self, s: str) -> int: 
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1  # always do so
        dp[1] = 1
        for i in range(2, n+1):
            if s[i-1] != '0':  # current one valid:
                dp[i] = dp[i-1]
            if 10 <= int(s[i-1]) + int(s[i-2]) * 10 <=26:
                dp[i] += dp[i-2]  # 包含 dp[i] = dp[i-1] + dp[i-2] 和 dp[i] = dp[i-2]两种情况
        return dp[-1]
