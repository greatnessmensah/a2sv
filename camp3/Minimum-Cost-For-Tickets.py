class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for _ in range(max(days)+1)]
        
        for i in range(1, len(dp)):
            second = third = float('inf')
            if i not in days:
                dp[i] = dp[i-1]
            else:
                first = dp[i-1] + costs[0]
                if len(dp) >= 7:
                    second = dp[i-7] + costs[1]
                else:
                    second = costs[1]
                if len(dp) >= 30:
                    third = dp[i-30] + costs[2]
                else:
                    third = costs[2]
                    
                dp[i] = min(first, second, third)
                
        return dp[-1]
