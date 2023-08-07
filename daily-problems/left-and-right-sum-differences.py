class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        
        for idx in range(1, len(nums)):
            left[idx] = left[idx-1] + nums[idx-1]
            
        for idx in range(len(nums)-2, -1, -1):
            right[idx] = right[idx+1] + nums[idx+1]
            
        return [abs(left[idx]-right[idx]) for idx in range(len(nums))]
            
    
    """
    Time: O(N)
    Space: O(N)
    """