class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        # def  a bfs function since we are trying to find the shortest path between two functions
        rows = len(forest)
        cols = len(forest[0])
        
        
        def bfs(sr, sc, tr, tc):
            if sr == tr and sc == tc:
                return 0
            visited = [[False] * cols for i in range(rows)]
            queue = [(sr, sc, 0)] # current row, current column, current number of steps
            visited[sr][sc] = True
            
            while queue:
                r, c, steps = queue.pop(0)
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_r, new_c = r + dr, c + dc
                    if 0<= new_r < rows and 0 <= new_c < cols and not visited[new_r][new_c] and forest[new_r][new_c] != 0: 
                        # when you find it has to be steps + 1 since you took an extra step
                        if new_r == tr and new_c == tc:
                            return steps + 1
                        visited[new_r][new_c] = True
                        queue.append((new_r, new_c, steps + 1))
                        
                        
            return -1 # not reachable
        
        # keep all the trees 
        trees = []
        for r in range(rows): 
            for c in range(cols):
                h = forest[r][c]
                if forest[r][c] > 1:
                    trees.append((h, r, c))
                    
        trees = sorted(trees)
        
        sr, sc = 0, 0
        total_steps = 0
        
        for height, row, col in trees:
            steps = bfs(sr, sc, row, col)
            if steps == -1:
                return -1 # cannot reach this tree
            
            total_steps += steps
            
            forest[row][col] = 1
            sr, sc = row, col 
            
        return total_steps