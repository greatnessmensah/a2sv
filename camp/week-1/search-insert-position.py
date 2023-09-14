class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums) - 1
        
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] <= target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
                
#         return left
        
        
        left, right = 0, len(nums)-1
        best = len(nums)
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid -1
                best = mid
            else:
                left = mid + 1
       
        return best
