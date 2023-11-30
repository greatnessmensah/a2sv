class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        orig = image[sr][sc]
        visited = set()
        
        def inbound(r, c):
            nonlocal m, n, orig
            if 0 <= r < m and 0 <= c < n:
                if (r, c) not in visited:
                    if image[r][c] != color and image[r][c] == orig:
                        return True
                    
        def dfs(row, col):
            if inbound(row, col):
                visited.add((row, col))
                image[row][col] = color

                dfs(row-1, col)
                dfs(row+1, col) 
                dfs(row, col-1) 
                dfs(row, col+1)
                
        dfs(sr, sc)
        return image
                
