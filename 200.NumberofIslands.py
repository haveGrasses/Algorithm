from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j, m, n)
        return res
    
    def dfs(self, grid, x, y, m, n):
        """ 从grid[x][y] 开始 flood-fill """
        # 主意`grid[x][y] != '1'`这里是字符串比较
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != '1':
            return 
        
        grid[x][y] = '#'
        
        self.dfs(grid, x+1, y, m, n)
        self.dfs(grid, x-1, y, m, n)
        self.dfs(grid, x, y-1, m, n)
        self.dfs(grid, x, y+1, m, n)
