class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        down = [0] * (len(grid[0])+2)
        top = [0] * (len(grid[0])+2)
        
        for i in range(1, len(down)-1):
            down[i] +=  down[i-1] + grid[1][i-1]
            
        for i in range(len(top)-2, 0,-1):
            top[i] += top[i+1] + grid[0][i-1]
            
        p_grid = [top,down]
        
        res = []
        
        for i in range(1, len(top)-1):
            res.append(max(top[i+1], down[i-1]))
            
        return min(res)
        
        
        
        