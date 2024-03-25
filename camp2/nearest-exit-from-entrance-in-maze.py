class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        queue = deque([[entrance[0], entrance[1], 0]])
        
        def valid(r, c):
            cell = (r, c)
            
            if not (0 <= r < n and 0 <= c < m):
                return False
            if maze[r][c] == "+":
                return False
            
            return True
        
        while queue:
            r, c, l = queue.popleft()
            if not valid(r, c):
                continue
            maze[r][c] = "+"
            
            if (r == 0 or r == n-1 or c == 0 or c == m-1) and [r,c] != entrance:
                return l
            
            for t, s in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                if not valid(r+t, c+s):
                    continue
                queue.append([r+t, c+s, l+1])

        return -1
            
        
        
