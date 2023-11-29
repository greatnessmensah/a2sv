class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        
        def inbound(r, c):
            nonlocal m, n
            if 0 <= r < m and 0 <= c < n:
                if (r, c) not in visited:
                    if grid[r][c] == "1":
                        return True
                    
        def dfs(row, col):
            if inbound(row, col):
                visited.add((row, col))

                dfs(row-1, col)
                dfs(row+1, col) 
                dfs(row, col-1) 
                dfs(row, col+1)
                
        count = 0
        for i in range(m):
            for j in range(n):
                if inbound(i, j):
                    dfs(i,j)
                    count+=1
                    
        return count
