# 事实证明短的代码不一定是好的，下面这个循环一点也不好理解和解释，也不具备扩展性，二下下个方法遇到不同的情况相应的改变dp的初始值就行
class Solution:
    def jumpFloor(self, number):
        dp1, dp2 = 0, 1
        for i in range(number):
            dp1, dp2 = dp2, dp1 + dp2
        return dp2


class Solution:
    def jumpFloor(self, number):
        if number <= 1:  # 这个去掉也行，因为0返回的值是0还是1都无所谓了
            return number
        dp1, dp2 = 1, 1  # 和Fibonacci数列不同的地方是跳0级台阶也有1种方法，他这个每次输出的数都和Fibonacci不同，只不过是Fibonacci的递推形式
        for i in range(2, number + 1):
            dp1, dp2 = dp2, dp1 + dp2
        return dp2


print(Solution().jumpFloor(0))  # 1
print(Solution().jumpFloor(2))  # 2
