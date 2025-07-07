class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # depth first search: return the true if a path is found

        def dfs(board, word, row, col, idx):
            if idx == len(word):
                return True
            
            if not 0<= row < len(board) or not 0 <= col < len(board[0]) or board[row][col] != word[idx]:
                return False
            
            board[row][col] = '#' # temp mark as visited

            res = (dfs(board, word, row+1, col, idx+1) or 
            dfs(board, word, row -1, col, idx+1) or 
            dfs(board, word, row, col + 1, idx + 1) or 
            dfs(board, word, row, col - 1, idx+ 1) )

            board[row][col] = word[idx]
            return res

        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                cell = board[i][j]
                if cell == word[0]:
                    if dfs(board, word, i, j, idx=0):
                        return True
        return False