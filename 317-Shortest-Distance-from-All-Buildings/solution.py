class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        bs = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bs.add(i * n + j)
        distance = [[0 for j in range(n)] for i in range(m)]
        count = [[0 for j in range(n)] for i in range(m)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for b in bs:
            queue = [b]
            cur_len = 0
            visited = [[False for j in range(n)] for i in range(m)]
            visited[b / n][b % n] = True
            while queue:
                size = len(queue)
                for s in range(size):
                    cur = queue.pop(0)
                    i, j = cur / n, cur % n
                    distance[i][j] += cur_len
                    count[i][j] += 1
                    for d in directions:
                        x, y = i + d[0], j + d[1]
                        if self.isValid(x, y, m, n, grid, visited):
                            queue.append(x * n + y)
                            visited[x][y] = True
                            
                cur_len += 1
        result = sys.maxint
        for i in range(m):
             for j in range(n):
                 if grid[i][j] == 0 and count[i][j] == len(bs):
                     result = min(result, distance[i][j])
        if result == sys.maxint:
            return -1
        return result
        
    def isValid(self, x, y, m, n, grid, visited):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        if visited[x][y]:
            return False
        if grid[x][y] != 0:
            return False
        return True
