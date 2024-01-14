class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        
        while i < len(nums):
            if nums[i] != i + 1:
                idx = nums[i] - 1
                if nums[i] != nums[idx]:
                    nums[i], nums[idx] = nums[idx], nums[i]
                else:
                    i += 1
            else:
                i += 1
                
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])
                
        return res
