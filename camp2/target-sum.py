class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(i, summ):
            if i >= len(nums):
                if summ == target:
                    return 1
                else:
                    return 0
            
            count = 0
            state = (i, summ)
            
            if state not in memo:
                pos = dp(i+1, summ + nums[i])
                neg = dp(i+1, summ - nums[i])
                count += (pos+neg)
                memo[state] = count
                
            return memo[state]
        
        memo = defaultdict(int)
        
        return dp(0, 0)
            
            
