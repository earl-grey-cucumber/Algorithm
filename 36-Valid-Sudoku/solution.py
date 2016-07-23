class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False
        m, n = len(board), len(board[0])
        rows = [[False for j in range(m)] for i in range(n)]
        cols = [[False for j in range(m)] for i in range(n)]
        block = [[False for j in range(m)] for i in range(n)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    val = int(board[i][j]) - 1
                    if rows[i][val]:
                        return False
                    else:
                        rows[i][val] = True
                    if cols[j][val]:
                        return False
                    else:
                        cols[j][val] = True
                    if block[(i / 3) * 3 + j / 3][val]:
                        return False
                    else:
                        block[(i / 3) * 3 + j / 3][val] = True
        return True
        