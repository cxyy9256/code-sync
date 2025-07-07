class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        # Strategy: DFS + Memoization
        if not matrix or not matrix[0]: # checks for matrix = [] or matrix = [[]]
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        memorize = [[0] * cols for _ in range(rows)]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        
        def dfs(r, c):
            # 2D cache (same size as matrix) that stores the length of the longest increasing path starting from each cell.
            if memorize[r][c] != 0:
                return memorize[r][c] # cache already computed
            max_len = 1
            
            for dx, dy in directions:
                new_r, new_c = r + dx, c + dy
                if (0 <= new_r < rows and 0 <= new_c < cols and matrix[new_r][new_c] > matrix[r][c]):
                    length = 1 + dfs(new_r, new_c)
                    max_len = max(max_len, length)
                
            memorize[r][c] = max_len
            return max_len
            
        max_path = 0
        
        for r in range(rows):
            for c in range(cols):
                max_path = max(max_path, dfs(r, c))
        
        return max_path