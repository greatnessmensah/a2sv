class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[-1] = matrix[-1].copy()
        
        def is_valid(r, c):
            if 0 <= r < n and 0 <= c < n:
                return dp[r][c]
            else:
                return float("inf")
            
        for r in range(n-2, -1, -1):
            for c in range(n-1, -1, -1):
                dp[r][c] += matrix[r][c]
                mini = min(is_valid(r+1, c-1), is_valid(r+1, c), is_valid(r+1, c+1))
                
                if mini != float("inf"):
                    dp[r][c] += mini
                    
        return min(dp[0])
