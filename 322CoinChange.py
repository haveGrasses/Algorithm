class Solution:
    def coinChange(self, coins, amount):
      """ iterative dp method """
        max_cnt = float('inf')
        dp = [0] + [max_cnt] * amount  # dp[i]: minimal coin numbers of amount i, when amount is 0, numbers is 0 as well.
        
        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        return [dp[amount], -1][dp[amount] == max_cnt]
