class Solution:
    """ python 2 passed, python 3 memeory limited error"""
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # how to calc numbers of 0 and numbers of 1 in a str:
        # 1st
        # for s in strs:
        #     ones = s.count('1')
        #     zeros = len(s) - ones  
        
        # 2nd
        # for ones, zeros in [(s.count('1'), s.count('0')) for s in strs]:
        
        # 3rd: [(sum(1 for c in s if c == '0'), sum(1 for s in s if c == '1')) for c in strs]
        # 4th
        for ones, zeros in map(lambda s: [s.count('1'), s.count('0')], strs):
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
        return dp[m][n]
    # the lower bound in for loop: when i < zeros, it means that with current i, i cannot form this str, so won't update dp
    # it keeps the value of the last result, the same is of j
    
    def findMaxForm2(self, strs, m, n):
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        def count(s):
            return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')
        
        for z, o in [count(s) for s in strs]:
            for x in range(m, -1, -1):
                for y in range(n, -1, -1):
                    if x >= z and y >= o:
                        dp[x][y] = max(1 + dp[x-z][y-o], dp[x][y])
                        
        return dp[m][n]
    
    # TODO: greedy algorithm


s = Solution()
print(s.findMaxForm(["10","0001","111001","1","0"], 5, 3))
print(s.findMaxForm2(["10","0001","111001","1","0"], 5, 3))
