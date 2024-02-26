class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dp(num):
            if num == target:
                return 1
            if num > target:
                return 0
            
            if num not in memo:
                for c in nums:
                    memo[num] += dp(c+num)
                    
            return memo[num]
        
        memo = defaultdict(int)
        return dp(0)
                    
