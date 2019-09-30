"""
Calculate and maintain 2 DP states:

pal[i][j] , which is whether s[i..j] forms a pal

d[i], which
is the minCut for s[i..n-1]

Once we comes to a pal[i][j]==true:

if j==n-1, the string s[i..n-1] is a Pal, minCut is 0, d[i]=0;
else: the current cut num (first cut s[i..j] and then cut the rest
s[j+1...n-1]) is 1+d[j+1], compare it to the existing minCut num
d[i], replace if smaller.
d[0] is the answer.
"""

class Solution:
    """
    valid[i][j]: whether s[i][j] can form a palindrome
    dp[i]: min cut for s[i:]
    transformation:
        if valid[i][j]: dp[i] = min(dp[i], 1+dp[j+1])  # 注意处理j+1越界的情况，此时dp[i]应为0
    """
    def minCut(self, s: str) -> int:
        valid = [[0 for _ in range(len(s))] for _ in range(len(s))]
        dp = [len(s) - i - 1 for i in range(len(s))]  # 上限就是每个字母都单独构成一个回文
        for i in range(len(s)-1, -1, -1):  # 这里是从后向前扫，也有从前向后的做法
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or valid[i+1][j-1]):  # 注意在dp下是如何判断s[i..j]是否是回文的，一点点往外扩，只需要看上一次[i+1][j-1]位置是否为True
                    valid[i][j] = 1
                    if j == len(s) - 1:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], 1 + dp[j+1])
        return dp[0]


print(Solution().minCut("aab"))
