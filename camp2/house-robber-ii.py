class Solution:
    def rob(self, nums: List[int]) -> int:
        res = []
        
        if len(nums) == 1:
            return nums[0]
        
        def dp(i):
            if i >= len(pos):
                return 0
            
            if i not in memo:
                memo[i] = max(dp(i+2)+pos[i], dp(i+1))
                
            return memo[i]
        
        memo = defaultdict(int)
        pos = nums[:-1]
        res.append(dp(0))
        
        memo = defaultdict(int)
        pos = nums[1:]
        res.append(dp(0))
        
        return max(res)
