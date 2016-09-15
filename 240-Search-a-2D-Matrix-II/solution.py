class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def helper(matrix, target, up, down, left, right):
            if up > down or left > right:
                return False
            mid = (left + right) / 2
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return helper(matrix, target, row, down, left, mid - 1) or helper(matrix, target, up, row - 1, mid + 1, right)
                
        m, n = len(matrix), len(matrix[0])
        return helper(matrix, target, 0, m - 1, 0, n - 1)