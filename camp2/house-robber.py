class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            if i >= len(nums):
                return 0
            
            if i not in memo:
                memo[i] = max(dp(i+2) + nums[i], dp(i+1))
            
            return memo[i]
        
        memo = {}
        return dp(0)
    
