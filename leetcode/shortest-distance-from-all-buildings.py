class Solution(object):
    from collections import deque
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """


        # bfs since we want the 
        if not grid or not grid[0]:
            return -1
        
        row, col = len(grid), len(grid[0])

        # reach[r][c] = X, For each empty land cell (r, c), this keeps track of how many buildings could reach this land cell. this should = the total number of buildings since we need to reach all the buildings for it to be valid

        # dist[r][c] = X; for each empty land cell (r, c), this keeps a running total of the shortest distances from all buildings to that cell.

        # for each of the reaches that == the total number of buildings, pull out the dist 
        dist = [[0] * col for _ in range(row)] # creates m by n matrix
        reach = [[0] * col for _ in range(row)]
        building_count = 0

        def bfs(start_r, start_c):
            visited = [[False] * col for _ in range(row)]
            # third param is the length of the path
            queue = deque([(start_r, start_c, 0)])
            visited[start_r][start_c] = True

            while queue:
                r, c, d = queue.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc]:
                        if grid[nr][nc] == 0:
                            visited[nr][nc] = True
                            dist[nr][nc] += d + 1 # d is all the distance to get to that empty land from one of the building when this is called
                            reach[nr][nc] += 1
                            queue.append((nr, nc, d+1))
        
        # count how many buildings there are and how many building can be reached by each spot 

        # Find an empty land cell that can reach all buildings in the shortest total travel distance. because of this we want to find From each building, compute the shortest path to every empty land.
        # populate reach[r][c] and dist
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    building_count += 1
                    bfs(r, c)
        
        # minimum travel distance of the new house
        result = float('inf')
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0 and reach[r][c] == building_count:
                    result = min(result, dist[r][c])

        return result if result != float('inf') else -1