class Solution(object):
    def fib(self, N):
        a, b = 0, 1
        for i in range(N):
            a, b = b, a+b
        return a
        
