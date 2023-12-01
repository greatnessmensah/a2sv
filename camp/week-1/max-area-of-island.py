class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        maxi = 0
        
        
        def inbound(r, c):
            nonlocal m,n 
            if 0 <= r < m and 0 <= c < n:
                if (r, c) not in visited:
                    if grid[r][c] == 1:
                        return True
                    
        def dfs(row, col):
            if inbound(row, col):
                visited.add((row, col))

                count = 1
                
                count += dfs(row-1, col)
                count += dfs(row+1, col) 
                count += dfs(row, col-1) 
                count += dfs(row, col+1)
                    
                return count
            return 0
        
        maxi, area = 0, 0
        for i in range(m):
            for j in range(n):
                area = dfs(i, j)
                maxi = max(maxi, area)
                
        return maxi
                    
