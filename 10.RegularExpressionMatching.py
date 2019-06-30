class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if (not s) or (not p):
        #     return False
        
        m, n = len(s), len(p)
        dp = [[0 for _ in range(n+1)] for _ in range(m+2)]
        dp[0][0] = True  # empty p matches empty s
        
        # is non-empty p match empty s: len(p) is even, current ele is `*`, previous ele is `.`
        # len(p)是even等价于dp[0][j]对应的j是even，j对应到p上是j-1，是odd
        for j in range(2, n+1, 2):  # j is even
            dp[0][j] = p[j-1] == '*' and dp[0][j-2]
            # 等价的写法：
            # if p[j-1] == '*':
            #     dp[0][j] = dp[0][j-2]
              
        # for j in range(1, n, 2):  # j is odd，对应到s和p上是even
        #     dp[0][j+1] = p[j] == '*' and p[j-1] == '.' and dp[0][j-1]
        
        # 上面两个循环一样的效果，注意的是dp里面的索引和对应的字符串是有偏移的
        
        # 理解一下这种解法，不考虑是奇数还是偶数，好理解一些，但是循环的次数也多了，用非空的p匹配空s
        # 只有可能是.*二者进行组合，
        # for j in range(1, n+1):  # 可以改成range(2, n+1)
        #     if p[j-1] == '*':  # 只有当当前的p是*的情况下才有可能变成True
        #         dp[0][j] = dp[0][j-2]  # 如果j不是偶数 这样更新的结果还是False
        
        # dp[i][j]对应的是s[i-1], p[i-1] 因为dp多了一个dp[0][0]的base condition
        
        # if not s:
        #     return bool(dp[0][n])
        # 
        # if not p:
        #     return False
        # 
        for i in range(1, m+1):
            for j in range(1, n+1):
                curS = s[i-1]
                curP = p[j-1]
                if curS == curP or curP == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif curP == '*': 
                    # `*`的前一个字符匹配到了最后一个s，说明`*`有可能匹配一次，当前的dp[i][j]取决于前j-1个p能否匹配到s-1
                    dp[i][j] |= dp[i][j-2] # * match 0 time
                    # * match 1 or more times
                    dp[i][j] |= dp[i-1][j] and (p[j-2] == '.' or p[j-2] == curS)
                    
        return bool(dp[m][n])
