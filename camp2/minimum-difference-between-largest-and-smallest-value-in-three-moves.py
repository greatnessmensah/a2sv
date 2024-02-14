class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        
        nums.sort()
        res = []
        left = 0
        right = len(nums) - 4
        
        while right < len(nums):
            res.append(nums[right]-nums[left])
            left += 1
            right += 1
            
        return min(res)
