from heapq import *
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0
        m, n = len(heightMap), len(heightMap[0]) 
        visited = [[False for j in range(n)] for i in range(m)]
        queue = []
        for i in range(m):
            visited[i][0], visited[i][n - 1] = True, True
            queue.append([heightMap[i][0], i, 0])
            queue.append([heightMap[i][n - 1], i, n - 1])
        for j in range(n):
            visited[0][j], visited[m - 1][j] = True, True
            queue.append([heightMap[0][j], 0, j])
            queue.append([heightMap[m - 1][j], m - 1, j])
        heapify(queue)
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        result = 0
        while queue:
            cell = heappop(queue)
            for dir in dirs:
                row, col = cell[1] + dir[0], cell[2] + dir[1]
                if 0 <= row < m and 0 <= col < n and not visited[row][col]:
                    visited[row][col] = True
                    result += max(0, cell[0] - heightMap[row][col])
                    update_height = max(cell[0], heightMap[row][col])
                    heappush(queue, [update_height, row, col])
        return result