class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         for num in range(len(nums)):
#             if num not in nums:
#                 return num
            
#         return len(nums)

        n = len(nums)
        result = (n * (n+1)) // 2
        
        for num in nums:
            result -= num
            
        return result
