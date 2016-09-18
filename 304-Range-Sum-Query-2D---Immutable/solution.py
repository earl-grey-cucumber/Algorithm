class NumMatrix(object):
    def __init__(self, matrix):
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        self.sums = [[0 for j in range(n)] for i in range(m)]
        self.sums[0][0] = matrix[0][0]
        for i in range(1, m):
            self.sums[i][0] = self.sums[i - 1][0] + matrix[i][0]
        for j in range(1, n):
            self.sums[0][j] = self.sums[0][j - 1] + matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                self.sums[i][j] = self.sums[i][j - 1] + self.sums[i - 1][j] + matrix[i][j] - self.sums[i - 1][j - 1]
# Time O(m*n). Space O(m*n)

    def sumRegion(self, row1, col1, row2, col2):
        upleft, up, left = 0, 0, 0
        if row1 == 0 and col1 != 0:
            up = 0
            left = self.sums[row2][col1 - 1]
        if col1 == 0 and row1 != 0:
            up = self.sums[row1 - 1][col2] # not sums[row1 - 1][0]
            left = 0
        if row1 != 0 and col1 != 0:
            upleft = self.sums[row1 - 1][col1 - 1]
            up = self.sums[row1 - 1][col2]
            left = self.sums[row2][col1 - 1]
        result = self.sums[row2][col2] + upleft - up - left
        return result

        


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)