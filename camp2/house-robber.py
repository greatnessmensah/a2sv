class Solution:
    def rob(self, nums: List[int]) -> int:
#         def dp(i):
#             if i >= len(nums):
#                 return 0
            
#             if i not in memo:
#                 memo[i] = max(dp(i+2) + nums[i], dp(i+1))
            
#             return memo[i]
        
#         memo = {}
#         return dp(0)
    
        dp = [0, 0]
        
        for i in range(len(nums)):
            temp = max(dp[-1]+nums[i], dp[-2])
            dp[-1] = dp[-2]
            dp[-2] = temp
            
        return dp[-2]
