class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        result, rowhit, colhit = 0, 0, [0] * n
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j - 1] == 'W':
                    rowhit = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        #if grid[i][k] == 'E':
                        rowhit += grid[i][k] == 'E'
                        k += 1
                if i == 0 or grid[i - 1][j] == 'W':
                    colhit[j] == 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        #if grid[k][j] == 'E':
                        colhit[j] += grid[k][j] == 'E'
                        k += 1
                if grid[i][j] == '0':
                    result = max(result, rowhit + colhit[j])
        return result
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        result = 0
        colhits = [0] * n
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if j == 0 or row[j-1] == 'W':
                    rowhits = 0
                    k = j
                    while k < n and row[k] != 'W':
                        rowhits += row[k] == 'E'
                        k += 1
                if i == 0 or grid[i-1][j] == 'W':
                    colhits[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        colhits[j] += grid[k][j] == 'E'
                        k += 1
                if cell == '0':
                    result = max(result, rowhits + colhits[j])
        return result
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        v1, v2 = [[0 for j in range(n)] for i in range(m)], [[0 for j in range(n)] for i in range(m)]
        v3, v4 = [[0 for j in range(n)] for i in range(m)], [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                cand1 = 0 if (j == 0 or grid[i][j] == 'W') else v1[i][j - 1]
                v1[i][j] = cand1 + 1 if grid[i][j] == 'E' else cand1
            for j in range(n - 1, -1, -1):
                cand2 = 0 if (j == n - 1 or grid[i][j] == 'W') else v2[i][j + 1]               
                v2[i][j] = cand2 + 1 if grid[i][j] == 'E' else cand2
        for j in range(n):
            for i in range(m):
                cand3 = 0 if (i == 0 or grid[i][j] == 'W') else v3[i - 1][j]
                v3[i][j] = cand3 + 1 if grid[i][j] == 'E' else cand3
            for i in range(m - 1, -1, -1):
                cand4 = 0 if (i == m - 1 or grid[i][j] == 'W') else v4[i + 1][j]
                v4[i][j] = cand4 + 1 if grid[i][j] == 'E' else cand4
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res, v1[i][j] + v2[i][j] + v3[i][j] + v4[i][j])
        return res
        """