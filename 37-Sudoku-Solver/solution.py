class Solution(object):
    def solveSudoku(self, board):
        if not board:
            return
        self.dfs(board, 0, 0)
        
    def dfs(self, board, x, y):
        if x == 9:
            return True
        if board[x][y] == ".":
            nextx, nexty = x, y + 1
            if nexty == 9:
                nextx = x + 1
                nexty = 0
            for i in range(9):
                cand = str(i + int("1"))
                if self.isvalid(board, x, y, cand):
                    board[x][y] = cand
                    if self.dfs(board, nextx, nexty):
                        return True
                    else:
                        board[x][y] = "."
            return False
        else:
            nextx, nexty = x, y + 1
            if nexty == 9:
                nextx = x + 1
                nexty = 0
            return self.dfs(board, nextx, nexty)
            
    def isvalid(self, board, x, y, cand):
        for i in range(9):
            if board[x][i] == cand:
                return False
            if board[i][y] == cand:
                return False
        for i in range(3):
            for j in range(3):
                if board[(x/3)*3+i][(y/3)*3+j] == cand:
                    return False
        return True
