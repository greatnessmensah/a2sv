class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        if grid[0][0] == 1:
            queue = deque([[0,0,k-1,0]])
        else:
            queue = deque([[0,0,k,0]])

        visited = set([(0,0,k)])

        while queue:
            r, c, curr, step = queue.popleft()

            if r == len(grid) -1 and c == len(grid[0]) - 1:
                return step
            
            for a, b in directions:
                o = r + a
                p = c + b
                
                if inbound(o, p) and (o, p, curr-1) not in visited:
                    if grid[o][p] == 1 and curr > 0:
                        queue.append([o, p, curr-1, step+1])
                        visited.add((o, p, curr-1))
                    elif grid[o][p] == 0:
                        queue.append([o,p, curr, step+1])
                        visited.add((o, p, curr-1))

        return -1
