class Solution(object):
    def uniquePaths(self, m, n):
        """ using dp, seemingly not that horrible
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp = [[1 for x in range(n)] for x in range(m)]  # others
        dp = [[1]*n]*m  # m row n col, looks cleaner than above, faster?
        # the initial value is 1, cause dp[0][j] = dp[i][0]
        # the loop from index 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[-1][-1]  # others
        return dp[m-1][n-1]
        
