class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n
        
        def dp(r, c):
            if not inbound(r, c):
                return 0
            
            if r == m -1 and c == n -1:
                return 1
            
            state = (r, c)
            
            if state not in memo:
                right = dp(r+1, c)
                down = dp(r, c+1)
                memo[state] = right + down
                
            return memo[state]
        
        memo = defaultdict(int)
        
        return dp(0, 0)
