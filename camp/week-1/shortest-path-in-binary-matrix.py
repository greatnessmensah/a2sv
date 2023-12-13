class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        end = (len(grid)-1, len(grid)-1)
        visited = set([(0, 0)])
        queue = deque([(0, 0, 1)])
        step = 0
        
        
        if grid[0][0] == 1:
            return -1
        
        def inbound(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid):
                if (row, col) not in visited:
                    if grid[row][col] == 0:
                        return True
        
        while queue:
            r, c, level = queue.popleft()
            
            if (r, c) == end:
                return level
            
            for x, y in [(r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r-1, c-1), (r-1, c+1), (r+1, c-1)]:
                if inbound(x, y):
                    queue.append((x, y, level+1))
                    visited.add((x, y))
                          
        return -1
                        
        
