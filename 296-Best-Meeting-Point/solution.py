class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x, y = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
        sumx, sumy, size = 0, 0, len(x)
        for i in range(size):
            sumx += abs(x[i] - x[size / 2])
        y = sorted(y)
        for i in range(size):
            sumy += abs(y[i] - y[size / 2])
        return sumx + sumy
            