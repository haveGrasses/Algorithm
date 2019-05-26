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


class Solution:
    """ bottom up, CAUTION: a false solution! """
    def knapsack(self, w, v, C):
        n = len(w)
        # dp = [[0 for _ in range(C+1)] for _ in range(n)]
        dp = [
            [0 if w[0] > j else v[0] for j in range(C+1)]
            for _ in range(n)
        ]  # let all row be the same as row 0
        
        # dp: row i: the ith item, col j: the capacity j
        # dp[i][j]: the best value we can get using the first i item if the capacity limit is j
        
        # bottom up, the bottom case
        # for row 0, the best value is the value of the 0th item if
        # the weight of the 0th item is smaller than column value else 0
        
        # for i in range(C+1):
        #     dp[0][i] = 0 if w[0] > C else v[0]
        
        for i in range(1, n):
            for j in range(w[i], C+1):  # note the start idx: for j=0 to w[i],
                # j-w[i] < 0: we don't bother to update these values 
                # these is a bug: these un-updated values is kept as the values of dp[0]
                # but it should be dp[i-1]
                dp[i][j] = max(dp[i-1][j], v[i] + dp[i-1][j-w[i]])
                
        return dp[-1][-1]
  

"""
i=2
[[ 0  6  6  6  6  6]
 [ 0  6 10 16 16 16]
 [ 0  6  6 16  6  6]]
-------
[[ 0  6  6  6  6  6]
 [ 0  6 10 16 16 16]
 [ 0  6  6 16 18  6]]
-------
[[ 0  6  6  6  6  6]
 [ 0  6 10 16 16 16]
 [ 0  6  6 16 18 22]]
-------
----------------------
the last row: [ 0  6  6 16 18 22]]
should be: [ 0  6 10 16 18 22]
because we do not loop j from 0, 
the unchanged part:[0  6  6 16 * *] is recorded as the row 0 

if we loop from 0, this can be fixed

so it prove that if we record dp as a 2-dimension array, there
is a lot of inefficient operations

if dp is 1-d array, this line `for j in range(w[i], C+1):` is right
"""
s = Solution()
w = [1, 2, 3]
v = [6, 10, 12]
print(s.knapsack(w, v, 5))


class Solution:
    """ bottom up, CAUTION: a false solution! """
    def knapsack(self, w, v, C):
        n = len(w)
        dp = [[0 for _ in range(C+1)] for _ in range(n)]
        
        for j in range(C+1):
            dp[0][j] = v[0] if j >= w[0] else 0
        
        for i in range(1, n):
            for j in range(C+1): 
                res = dp[i-1][j]  # dp[i][j] = dp[i-1][j]
                if j - w[i] >= 0:
                    res = max(res, v[i] + dp[i-1][j-w[i]])  # dp[i][j] = max(dp[i][j], v[i] + dp[i-1][j-w[i]])
                dp[i][j] = res
        return dp[-1][-1]


