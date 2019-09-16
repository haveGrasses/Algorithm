# LC
class Solution(object):
    def fib(self, N):
        a, b = 0, 1
        for i in range(N):
            a, b = b, a+b
        return a

# JZ
class Solution:
    """ 以前很喜欢的，现在2019-09-16很不喜欢的写法 """
    def Fibonacci(self, n):
        dp1, dp2 = 0, 1
        for i in range(n):  # 这里的循环次数
            dp1, dp2 = dp2, dp1+dp2
        return dp1  # 还有返回的是第一个...


class Solution:
    """ dp模板式的写法 """
    def Fibonacci(self, n):
        if n <= 1:
            return n
        dp1, dp2 = 0, 1
        for i in range(2, n+1):
            dp1, dp2 = dp2, dp1+dp2
        return dp2
