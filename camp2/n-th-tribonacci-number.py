class Solution:
    def tribonacci(self, n: int) -> int:
        def dp(i):
            if i == 0:
                return 0
            if i < 3:
                return 1
            
            if memo[i] == -1:
                memo[i] = dp(i-1) + dp(i-2) + dp(i-3)
                
            return memo[i]
            
        memo = [-1] * (37+1)
        
        return dp(n)
        
