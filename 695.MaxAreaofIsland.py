from typing import List


class Solution:
    """根据200改过来的，不是最好的，dfs的处理应该用累加的方法，不要连写4个等号"""
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j, m, n, 0)
                    res = max(res, area)
        return res
    
    def dfs(self, grid, i, j, m, n, area):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
            return area
        
        area += 1
        grid[i][j] = '#'
        
        area = self.dfs(grid, i+1, j, m, n, area)
        area = self.dfs(grid, i-1, j, m, n, area)
        area = self.dfs(grid, i, j-1, m, n, area)
        area = self.dfs(grid, i, j+1, m, n, area)
        return area


class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = self.dfs(grid, i, j, m, n)
                    res = max(res, cnt)
        return res
    
    def dfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
            return 0
        grid[i][j] = '#'
        return 1 + self.dfs(grid, i-1, j, m, n) + self.dfs(grid, i+1, j, m, n) + \
               self.dfs(grid, i, j-1, m, n) + self.dfs(grid, i, j+1, m, n)
