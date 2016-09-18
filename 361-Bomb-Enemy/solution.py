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
        result, rowhit, colhit = 0, 0, [0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j - 1] == 'W':
                    rowhit = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            rowhit += 1
                        k += 1
                if i == 0 or grid[i - 1][j] == 'W':
                    colhit[j] == 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            colhit[j] += 1
                        k += 1
                if grid[i][j] == '0':
                    result = max(result, rowhit + colhit[j])
        return result
        """
        row_size = len(grid)
        col_size = len(grid[0]) if row_size else 0
        max_killed = 0
        row_e, col_e = 0, [0] * col_size
        for ri in xrange(row_size):
            for ci in xrange(col_size):

               # no need to re-calculate enemy if there is no wall behind unless it's a col=0
                if ci == 0 or grid[ri][ci-1] == 'W':
                    row_e = 0
                    for k in xrange(ci, col_size):
                        if grid[ri][k] == 'W': break
                        row_e += grid[ri][k] == 'E'

                # no need to re-calculate enemy if there is no wall behind unless it's a row=0
                # if wall is behind, start couting enemy
                if ri == 0 or grid[ri-1][ci] == 'W':
                    col_e[ci] = 0
                    for k in xrange(ri, row_size):
                        if grid[k][ci] == 'W': break
                        col_e[ci] += grid[k][ci] == 'E'

                # empty spot, check max_killed
                if grid[ri][ci] == '0':
                    max_killed = max(max_killed, row_e + col_e[ci])

        return max_killed
           
      
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