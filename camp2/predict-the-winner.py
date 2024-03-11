class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache
        def dp(left, right, turn):
            if left > right:
                return 0
            
            if turn:
                return max(dp(left+1, right, False) + nums[left], dp(left, right-1, False) + nums[right])
            else:
                return min(dp(left+1, right, True) - nums[left], dp(left, right-1, True) - nums[right])
        
        return dp(0, len(nums)-1, True) >= 0
