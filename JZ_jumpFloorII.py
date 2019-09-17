class Solution:
    """ 自己瞎写的居然过了... """
    def jumpFloorII(self, number):
        dp = [0 for _ in range(number+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, number+1):
            for j in range(i):
                dp[i] += dp[j]
        return dp[-1]

    def jumpFloorII2(self, number):
        """ 我jio得，还是上面那个解法好，这个看看就行 """
        dp = [1 for _ in range(number)]  # dp全初始化为1是想表达什么，可能是把从0台阶跳上来的那一步揉进来了吧，这样就不用每次循环的时候加一个dp[0]对应的1，所以dp也可以少写1个长度
        for i in range(1, number):
            for j in range(i):
                dp[i] += dp[j]
        return dp[-1]

    def jumpFloorII3(self, number):
        """ 等比数列的解法
        f(n) = 2*f(n-1)
        """
        cnt = 1
        for i in range(1, number):
            cnt *= 2
        return cnt

    def jumpFloorII4(self, number):
        """ 等比数列的解法,
        有了等比数列公比和首项，就不要再像jumpFloorII3一样去循环求了。。。
        """
        return 1*2**(number-1)


print(Solution().jumpFloorII(2))
print(Solution().jumpFloorII2(2))
