class Solution(object):
    def numIslands(self, grid):
        def dfs(grid, x, y, m, n):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == "0":
                return
            grid[x][y] = "0"
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for d in directions:
                dfs(grid, x + d[0], y + d[1], m, n)
        if not grid:
            return 0
        m, n, count = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, i, j, m, n)
                    count += 1
        return count
    

