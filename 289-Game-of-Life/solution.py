class Solution(object):
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if k == 0 and l == 0:
                            continue
                        x, y = i + k, j + l
                        if  0 <= x < m and 0 <= y < n and (board[x][y] & 1) == 1:
                            count += 1
                if count == 3 or (count == 2 and board[i][j] == 1):
                    board[i][j] |= 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1