
class Solution:
    """ dp，列是字符串，行是pattern，初始化后，两层循环，每次把当前遍历到的格子当成是最后一个s和最后一个p，
    当前的值分两种情况进行更新：
    1、当前的pattern匹配到了当前的s：当前字符相等或者当前p是`.`：此时当前dp的值取决于i-1和p-1格子的值
    2、当前的pattern没匹配上，这里又分两种，一是因为当前p是*没匹配上，这种是有救的，二是当前p是普通字符串，这种就不作为了，因为默认值就是False
    因此第二种情况可以简化为只考虑当前p是*的情况 加个if：
        1、*匹配1+次：前提是先匹配1次，即p[j-2] == s[i-1]或者p[j-2] == '.'，
        之后dp的更新考虑是仅匹配一次还是匹配1次以上，这两者是一样的，都依赖dp[i-1][j],
        为什么匹配1次和1次以上是一样的：匹配一次相当一在本轮匹配一次和在下一轮用p匹配0次，都是要在本轮匹配一次
        匹配多次是在本轮匹配一次，在下一次匹配多次
        2、*匹配0个字符：dp[i][j] = dp[i][j-2]
    """
    def isMatch(self, s: str, p: str) -> bool:
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
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                curS = s[i-1]
                curP = p[j-1]
                if curS == curP or curP == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif curP == '*': 
                    """这里面其实是一个if else，理解一下如何转换成现在的样子的"""
                    dp[i][j] |= dp[i][j-2] # * match 0 time
                    # * match 1 or more times
                    # `*`的前一个字符匹配到了最后一个s，说明`*`有可能匹配一次或更多，
                    # 如何描述匹配多次：仍然拿现在的p去匹配前i-1的s
                    dp[i][j] |= dp[i-1][j] and (p[j-2] == '.' or p[j-2] == curS)
                    
        return bool(dp[m][n])
