class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = 0
        arr = [0] * len(nums)
        
        for i in range(len(nums)):
            running_sum += nums[i]
            arr[i] = running_sum
            
        return arr