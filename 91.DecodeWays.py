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
            if 10 <= int(s[i-1]) + int(s[i-2]) * 10 <= 26:
                dp[i] += dp[i-2]  # 包含 dp[i] = dp[i-1] + dp[i-2] 和 dp[i] = dp[i-2]两种情况
        return dp[-1]

    
class Solution:
    def numDecodings(self, s: str) -> int: 
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp2, dp1 = 1, 1
        
        for i in range(2, n+1):
            dp = 0
            if s[i-1] != '0':  # current one valid:
                dp = dp1
            if 10 <= int(s[i-1]) + int(s[i-2]) * 10 <= 26:
                dp += dp2  # 包含 dp = dp1 + dp2 和 dp = dp2 两种情况
            dp2 = dp1  # 现更新dp2的值！因为dp2依赖没有更新的dp1的值
            dp1 = dp
        return dp1


class Solution:
    """ 从后往前扫 避免索引不对齐问题
    dp[i]的含义：s[i: ]的decode个数，就是以s[i]开头到结尾的数字的decode数量
    """
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        dp = [0 for _ in range(n + 1)]
        dp[n] = 1
        dp[n - 1] = 0 if s[n - 1] == '0' else 1
        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                continue  # 必须跟在前一个数的后面，以当前数开头到最后的解码方式就是0，不更新
            if 10 <= int(s[i]) * 10 + int(s[i + 1]) <= 26:
                dp[i] = dp[i + 1] + dp[i + 2]  # 一个数和两个数都valid
            else:
                dp[i] = dp[i + 1]  # 仅当前一个数valid
        return dp[0]

    # 其实上面for里面那个if-if-else也可以写成这样：
    # if s[i] != 0:
    #     dp[i] = dp[i+1]
    # if 10 <= int(s[i]) * 10 + int(s[i + 1]) <= 26:
    #     dp[i] += dp[i+2]

    def numDecodings2(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        dp = [0 for _ in range(n + 1)]
        dp[n] = 1
        dp[n - 1] = 0 if s[n - 1] == '0' else 1
        for i in range(n - 2, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i+1]
            if 10 <= int(s[i]) * 10 + int(s[i + 1]) <= 26:
                dp[i] += dp[i+2]
        return dp[0]


class Solution:
    """ 做一下改编后的A-Z从0开始编码的方式 """
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0 for _ in range(n + 1)]
        dp[n] = 1
        dp[n - 1] = 1
        for i in range(n - 2, -1, -1):
            dp[i] = dp[i+1]
            if 10 <= 10*int(dp[i]) + dp[i+1] <= 25:
                dp[i] += dp[i+2]
        return dp[0]


print(Solution().numDecodings('12'))
