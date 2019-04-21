class Solution(object):
    def uniquePaths(self, m, n):
        """ using dp, seemingly not that horrible
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for x in range(n)] for x in range(m)]  # others
        # dp = [[1]*n]*m  # m row n col, looks cleaner than above, faster? No! This is a line of danger
        # why: 
        """ It is the first time I feel insafe when using Python
        >>> dp = [[1, 1, 1]] * 4
        >>> dp
        [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
        >>> dp[1][1]=0
        >>> dp
        [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
        """
        
        # another example
        """
        >>> pre = cur = [1] * 4
        >>> pre
        [1, 1, 1, 1]
        >>> cur
        [1, 1, 1, 1]
        >>> cur[0] = 9
        >>> cur
        [9, 1, 1, 1]
        >>> pre
        [9, 1, 1, 1]
        """
        
        # the initial value is 1, cause dp[0][j] = dp[i][0]
        # the loop from index 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[-1][-1]  # others
        return dp[m-1][n-1]
    
    def uniquePaths2(self, m, n):
        """ only use 2 vector rathan a matrix """
        pre, cur = [1] * n, [1] * n  # not pre = cur = [1]*n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = cur[j-1] + pre[j]
            # print('pre:', pre)
            # print('cur', cur)
            pre, cur = cur, pre
            # print('------')
            # print('pre:', pre)
            # print('cur', cur, '\n')
        return pre[-1]
    
    # actually, when I use pre = cur = [1]*n, the swap operation can be omitted, this may be a side benefit?
    def uniquePaths4(self, m, n):
        pre = cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = cur[j-1] + pre[j]  # no swap operation, caz pre and cur always keeps same
        return pre[-1]
    
    def uniquePaths3(self, m, n):
        """ only use one single vector rather than two """
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]
    
