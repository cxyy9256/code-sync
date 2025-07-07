class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        def dfs(r, c):
            # check in bounds and is land
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            # mark land as 0 after visited
            board[r][c] = 'T'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            # left border
            if board[r][0] == 'O':
                dfs(r, 0)
            # right border
            if board[r][cols-1] == 'O':
                dfs(r, cols -1)

        for c in range(cols):
            # top border
            if board[0][c] == 'O':
                dfs(0, c)
            # bottom border
            if board[rows-1][c] == 'O':
                dfs(rows-1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'