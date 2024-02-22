class Solution:
    def tribonacci(self, n: int) -> int:
#         def dp(i):
#             if i == 0:
#                 return 0
#             if i < 3:
#                 return 1
            
#             if memo[i] == -1:
#                 memo[i] = dp(i-1) + dp(i-2) + dp(i-3)
                
#             return memo[i]
            
#         memo = [-1] * (37+1)
        
#         return dp(n)

        if n == 0:
            return n
        elif n < 3:
            return 1
        
        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = dp[2] = 1
        
        for i in range(3, len(dp)):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            
        return dp[n]
        
