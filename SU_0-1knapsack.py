class Solution:
    """  a top-down solution """
    def knapsack(self, w, v, C):
        """
        :param w: weight of every knapsack
        :param v: value
        :param C: capacity
        :return: best combination value 
        """
        n = len(w)
        memo = [[-1 for _ in range(C+1)] for _ in range(n)]
        
        return self.bestValue(w, v, n-1, C, memo)
    
    def bestValue(self, w, v, idx, c, memo):
        """
        考虑从[0, idx]的物品中，填充容量为c的背包能获得的最大价值
        """
        # basic condition
        if idx < 0 or c < 0:
            return 0  # 当没有物品或者没有容量时，最大价值都是0
        
        if memo[idx][c] != -1:
            return memo[idx][c]
        
        # 不考虑第idx个物品
        res = self.bestValue(w, v, idx-1, c, memo)
        # 考虑加入第idx个物品
        if c >= w[idx]:  # 首先判断背包是否能容纳下这个物品
            res = max(res, v[idx] + self.bestValue(w, v, idx-1, c-w[idx], memo))
        
        memo[idx][c] = res
        return res
        

s = Solution()  
w = [1, 2, 3]
v = [6, 10, 12]
print(s.knapsack(w, v, 5))
