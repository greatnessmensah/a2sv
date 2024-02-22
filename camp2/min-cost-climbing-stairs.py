class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
#         def dp(idx):
#             if idx == len(cost)-1 or idx == len(cost)-2:
#                 return cost[idx]

#             if memo[idx] == -1:
#                 one = dp(idx+1)
#                 two = dp(idx+2)
#                 memo[idx] = min(one, two) + cost[idx]
#             return memo[idx]
            
#         memo = [-1] * len(cost)
#         a = dp(0)
#         b = dp(1)
#         return min(a, b)


        dp = [0 for _ in range(len(cost)+1)]
        dp[-2] = dp[-3] = cost[-1]
        
        for i in range(len(cost)-2, -1, -1):
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
            
        return min(dp[0], dp[1])

            
        
