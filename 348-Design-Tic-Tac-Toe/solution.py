class TicTacToe(object):

    def __init__(self, n):
        self.dig1, self.dig2 = [0, 0], [0, 0]
        self.rows, self.cols = [[0, 0] for i in range(n)], [[0, 0] for i in range(n)]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        i, n = player - 1, len(self.rows)
        self.rows[row][i] += 1
        self.cols[col][i] += 1
        if row == col:
            self.dig1[i] += 1
        if row + col == n - 1: # not elif, some point may in both diagonals, also it’s n - 1
            self.dig2[i] += 1
        if any([self.rows[row][i] == n, self.cols[col][i] == n, \
self.dig1[i] == n, self.dig2[i] == n]):
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)