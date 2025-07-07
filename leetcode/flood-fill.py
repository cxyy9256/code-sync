class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        original_color = image[sr][sc]
        
        if original_color == color:
            return image
        rows = len(image)
        cols = len(image[0])
        
        def dfs(r, c):
            if not 0 <= r < rows or not 0<= c < cols or image[r][c] != original_color:
                return
            
            # if it is the original color, turn it into the new color
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # just modify in place
        dfs(sr, sc)
        return image