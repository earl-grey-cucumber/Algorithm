class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        def dfs(matrix, i, j, m, n, dp):
            if dp[i][j] > 0:
                return dp[i][j]
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in directions:
                x, y = i + d[0], j + d[1]
                if 0 <= x < m and 0 <= y < n and matrix[i][j] < matrix[x][y]:
                    dp[i][j] = max(dp[i][j], dfs(matrix, x, y, m, n, dp))
            dp[i][j] += 1
            return dp[i][j]
            
        m, n, result = len(matrix), len(matrix[0]), 1
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(matrix, i, j, m, n, dp))
        return result