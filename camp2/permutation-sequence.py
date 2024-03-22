class Solution:
    def getPermutation(self, n: int, k: int) -> str:
#         nums = [i for i in range(1, n+1)]
#         perms = permutations(nums)
#         i = 1
        
#         for p in perms:
#             if i == k:
#                 res = p
#                 break
#             i += 1
        
#         return "".join([str(i) for i in res])
        k -= 1
        p = 1
        nums = [i for i in range(1, n+1)]
        res = ""
        
        for i in range(1, n):
            p *= i   
        
        while True:
            res += str(nums[k//p])
            nums.pop(k//p)
            if len(nums) == 0:
                break
            k %= p
            p //= len(nums)
            
        return res
