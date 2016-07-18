class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        max_len = 1
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                max_len = max(max_len, self.dfs(matrix, i, j, dp))
        return max_len
    
    def dfs(self, matrix, i, j, dp):
        if dp[i][j]:
            return dp[i][j]
        m, n = len(matrix), len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and matrix[i][j] < matrix[x][y]:
                dp[i][j] = max(dp[i][j], self.dfs(matrix, x, y, dp))
        dp[i][j] += 1
        return dp[i][j]
        
