class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = r = 2
        
        while r < len(nums):
            if nums[l-2] != nums[r]:
                nums[l] = nums[r]
                l += 1
            r += 1
            
        return l