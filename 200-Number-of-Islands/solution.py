"""
class UnionFind(object):
    def __init__(self, size):
        self.f = [-1] * size
    
    def get_f(self, x):
        if self.f[x] == x:
            return x
        self.f[x] = self.get_f(self.f[x])
        return self.f[x]
        
    def merge(self, x, y):
        if self.f[x] == -1 or self.f[y] == -1:
            return False
        fx, fy = self.get_f(x), self.get_f(y)
        if fx == fy:
            return False
        else:
            self.f[x] = y
            return True

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if uf.f[i * n + j] == -1:
                        uf.f[i * n + j] = i * n + j
                        count += 1
                    for d in ds:
                        x, y = i + d[0], j + d[1]
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1' and uf.merge(i * n + j, x * n + y):
                            count -= 1
        return count
"""
class union_find(object):
    def __init__(self, size):
        self.f = [-1] * size
    
    def get_father(self, x):
        if self.f[x] == x:
            return x
        self.f[x] = self.get_father(self.f[x])
        return self.f[x]

    def merge(self, x, y):
        if self.f[x] == -1:
            return False
        if self.f[y] == -1:
            return False
        x = self.get_father(x)
        y = self.get_father(y)
        if x == y:
            return False
        else:
            self.f[x] = y
            return True
        
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        m, n, count = len(grid), len(grid[0]), 0
        uf = union_find(m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                cur = i * n + j
                if uf.f[cur] == -1:
                    uf.f[cur] = cur
                    count += 1
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for d in directions:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < m and  0 <= y < n and grid[x][y] == '1' and uf.merge(cur, x * n + y):
                        count -= 1
        return count

