class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(i):
            if i == 0:
                return 0
            if i < 0:
                return float("inf")
            
            mini = float("inf")
                    
            if i not in memo:
                for coin in coins:
                    mini = min(mini, 1 + dp(i - coin))
                memo[i] = mini
                
            return memo[i]
        
        memo = defaultdict(int)
        res = dp(amount)
        
        return res if res != float("inf") else -1
        
                
            
                
