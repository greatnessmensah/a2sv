class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        maxi = num
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                    maxi = max(maxi, int("".join(nums)))
                    nums[j], nums[i] = nums[i], nums[j]
        
        return maxi
        
        
        
