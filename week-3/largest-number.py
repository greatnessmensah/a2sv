class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        s_nums = [str(i) for i in nums]
        
        for i in range(len(s_nums)):
            for j in range(i+1, len(s_nums)):
                if int(s_nums[i] + s_nums[j]) < int(s_nums[j] + s_nums[i]):
                    s_nums[i], s_nums[j] = s_nums[j], s_nums[i]
                    
        return str(int("".join(s_nums)))