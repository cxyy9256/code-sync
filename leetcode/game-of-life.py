class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        """
        Do not return anything, modify board in-place instead.
        """
        # check each blocks num of live neighbors
        # encode transition on what it will turn, then turn all of them to what they will be
        # 0: dead to dead, 1: live to live, 2: live to dead, 3: dead to live
        m, n = len(board), len(board[0])
        def count_live_neighbors(x, y):
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            count = 0
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                # need to check == 2 since some neighbors are alr encoded as 2
                if 0 <= nx < m and 0<= ny <n and (board[nx][ny] == 1 or board[nx][ny] ==2):
                    count += 1
            return count
            
            # count the live neighbors, and encode
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)

                # currently live, encoding
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = 3
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board [i][j] = 1