class Solution(object):
    def wallsAndGates(self, rooms):
        INF = 2147483647
        if len(rooms) == 0:
            return
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, m, n)
        
    def dfs(self, rooms, i, j, m, n):
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and rooms[x][y] > rooms[i][j] + 1:
                rooms[x][y] = rooms[i][j] + 1
                self.dfs(rooms, x, y, m, n)
                    