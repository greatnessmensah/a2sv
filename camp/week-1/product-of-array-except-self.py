class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        create prefix and suffix product of nums
        append 1 to prefix front and 1 to suffix end
        compute prefix[i-1] * suffix[i+1]
        """
#         res = []
        
#         for i in range(len(nums)):
#             left, right = 1, 1
            
#             for j in range(i):
#                 left *= nums[j]
                
#             for k in range(i+1, len(nums)):
#                 right *= nums[k]
                
#             res.append(left*right)
                              
#         return res
        
        left = 1
        right = 1
        prefix = [1]
        suffix = [1]
        res = []
        
        for i in range(len(nums)):
            prefix.append(1*prefix[-1]*nums[i])
            
        for i in range(len(nums)-1,-1,-1):
            suffix.append(1*suffix[-1]*nums[i])
            
        suffix = suffix[::-1]
        for i in range(1, len(suffix)):
            res.append(1*prefix[i-1] * suffix[i])
        
        return res