class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        best = float("inf")
        
        while left <= right:
            mid = left + (right-left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
            if best > nums[mid]:
                best = nums[mid]
    
        return best
            
        