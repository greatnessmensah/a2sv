class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         def dp(i):
#             if i == 0:
#                 return 0
#             if i < 0:
#                 return float("inf")
            
#             mini = float("inf")
                    
#             if i not in memo:
#                 for coin in coins:
#                     mini = min(mini, 1 + dp(i - coin))
#                 memo[i] = mini
                
#             return memo[i]
        
#         memo = defaultdict(int)
#         res = dp(amount)
        
#         return res if res != float("inf") else -1

        if amount == 0:
            return 0
    
        dp = [float("inf") for _ in range(amount+1)]
        
        dp[0] = 0
        
        for i in range(1, amount+1):
            mini = float("inf")
            for coin in coins:
                if i - coin >= 0:
                    mini = min(mini, 1 + dp[i-coin])
            dp[i] = mini
                
        return dp[amount] if dp[amount] != float("inf") else -1
        
