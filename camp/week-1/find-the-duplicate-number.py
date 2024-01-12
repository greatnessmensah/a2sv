class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
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
                if i+1 > nums[i]:
                    return nums[i]
                
        return res
