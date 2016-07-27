class Solution(object):
    def wallsAndGates(self, rooms):
        INF = 2147483647
        if len(rooms) == 0:
            return
        m, n = len(rooms), len(rooms[0])
        queue = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append(i * n + j)
        while queue:
            cur = queue.pop(0) # no need of size, no need to check for -1, only update INF
            i, j = cur / n, cur % n
            for d in directions:
                newi, newj = i + d[0], j + d[1]
                if 0 <= newi < m and 0 <= newj < n and rooms[newi][newj] == INF:
                    rooms[newi][newj] = rooms[i][j] + 1
                    queue.append(newi * n + newj)
