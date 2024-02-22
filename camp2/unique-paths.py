class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#         def inbound(r, c):
#             return 0 <= r < m and 0 <= c < n
        
#         def dp(r, c):
#             if not inbound(r, c):
#                 return 0
            
#             if r == m -1 and c == n -1:
#                 return 1
            
#             state = (r, c)
            
#             if state not in memo:
#                 right = dp(r+1, c)
#                 down = dp(r, c+1)
#                 memo[state] = right + down
                
#             return memo[state]
        
#         memo = defaultdict(int)
        
#         return dp(0, 0)

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1
        
        def inbound(r, c):
            if  0 <= r < m and 0 <= c < n:
                return dp[r][c]
            else:
                return 0
            
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                dp[r][c] += inbound(r+1, c) + inbound(r, c+1)
                
        return dp[0][0]
