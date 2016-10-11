class Solution(object):
    def totalNQueens(self, n):
        #loc = [0] * n
        col = [False] * n
        d1 = [False] * (2 * n - 1)
        d2 = [False] * (2 * n - 1)
        count = [0]
        self.helper(0, n, col, d1, d2, count)
        return count[0]
        
    def helper(self, row, n, col, d1, d2, count):
        if row == n:
            count[0] += 1
            return
        for i in range(0, n):
            if col[i] or d1[i + row] or d2[n - 1 - row + i]:
                continue
            col[i], d1[i + row], d2[n - 1 - row + i] = True, True, True
            #loc[row] = i
            #if self.isValid(row, i, loc):
            self.helper(row + 1, n, col, d1, d2, count)
            col[i], d1[i + row], d2[n - 1 - row + i] = False, False, False