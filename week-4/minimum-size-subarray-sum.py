class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = float("inf")
        l = summed = 0
        
        for r in range(len(nums)):
            summed += nums[r]
            
            while summed >= target:
                mini = min(mini, r-l+1)
                summed -= nums[l]
                l += 1
                
        return mini if mini < float("inf") else 0
    
    
    """
    Time: O(N)
    Space: O(1)
    """