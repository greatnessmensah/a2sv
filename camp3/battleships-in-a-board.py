class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        ans = 0
        
        def is_valid(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        
        def dfs(r, c):
            if not is_valid(r, c):
                return
            
            if (r, c) in visited:
                return
            
            if board[r][c] == ".":
                return
            
            visited.add((r, c))
            
            dfs(r+1, c)
            dfs(r, c+1)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X" and (i, j) not in visited:
                    dfs(i, j)
                    ans += 1
                
        return ans
        
