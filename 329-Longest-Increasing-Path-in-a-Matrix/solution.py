class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix: 
            return 0
        m, n = len(matrix), len(matrix[0])
        dis = [[0 for j in xrange(n)] for i in xrange(m)]
        return max([self.dfs(i, j, m, n, matrix, dis) for j in xrange(n) for i in xrange(m)])
 
    def dfs(self, x, y, m, n, matrix, dis):
        if dis[x][y]: return dis[x][y]
        for dx, dy in ([(1, 0), (-1, 0), (0, 1), (0, -1)]):
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < m and ny >= 0 and ny < n and matrix[x][y] < matrix[nx][ny]:
                dis[x][y] = max(dis[x][y], self.dfs(nx, ny, m, n, matrix, dis))
        dis[x][y] += 1
        return dis[x][y]


                