class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        lower_sum = upper_sum = 0
        left = 0
        right = len(nums)-1
        
        nums.sort()
        
        while left < right:
            ans = nums[left] + nums[right]
            if ans >= lower:
                right -= 1
            else:
                lower_sum += right - left
                left += 1
                
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            ans = nums[left] + nums[right]
            if ans > upper:
                right -= 1
            else:
                upper_sum += right - left
                left += 1
                
                
        return upper_sum - lower_sum
        