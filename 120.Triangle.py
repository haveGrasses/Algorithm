class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        
        n = len(triangle)
        dp = triangle[n-1]
        for i in range(n-2, -1, -1):  # n-2:last layer do not need to optimize
            for j in range(i+1):  # node
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        print(dp)
        return dp[0]  # bottom-up方法，优化到最上层，加上第一个元素后的最小值位于第一个索引
