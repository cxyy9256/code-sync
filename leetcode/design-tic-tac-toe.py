class TicTacToe(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.rows = [0] * n # contains the sum of each row of the 
        self.cols = [0] * n # contains the sum of 
        self.diag = 0
        self.anti_diag = 0
        

    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        # If player == 1, we add +1. If player == 2, we add -1
        mark = 1 if player == 1 else -1
        self.rows[row] += mark
        self.cols[col] += mark
        
        if row == col:
            self.diag += mark
        if row + col == self.n -1:
            self.anti_diag += mark
            
        # checking for winnings
        # abs because it could be the player 2 with the bunch of -1's win
        if (abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag) == self.n or abs(self.anti_diag) == self.n):
            return player
        return 0
            
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)