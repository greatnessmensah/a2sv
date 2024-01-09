class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        
        while i < len(nums):
            if nums[i] != i and nums[i] < len(nums):
                idx = nums[i]
                
                nums[idx], nums[i] = nums[i], nums[idx]
            else:
                i += 1
            
        for i in range(len(nums)):
            if nums[i] != i:
                return i
            
        return len(nums)
            
