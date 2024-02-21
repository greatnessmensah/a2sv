class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        def dp(i):
            if i < 2:
                memo[i] = i
                return i
            
            if memo[i] == -1:
                if i % 2:
                    memo[i] = dp((i-1) // 2) + dp((i-1) // 2 + 1)
                else:
                    memo[i] = dp(i // 2)

            return memo[i]
        
        memo = [-1] * (n+1)
        
        for i in range(n, -1, -1):
            dp(i)
            
        return max(memo)
        
