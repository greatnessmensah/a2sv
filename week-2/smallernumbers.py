class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = sorted(nums)
        hashmap = defaultdict(int)
        
        for i in range(len(ans)-1,-1,-1):
            hashmap[ans[i]] = i
            
        for i in range(len(nums)):
            nums[i] = hashmap[nums[i]]
            
        return nums

"""
Time: O(Nlog(N))
Space: O(N)
"""
