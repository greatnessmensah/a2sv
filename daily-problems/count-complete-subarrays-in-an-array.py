class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = len(set(nums))
        left = count = 0
        window = defaultdict(int)
        
        for right in range(len(nums)):
            window[nums[right]] += 1
            
            while len(window) == target:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
                
            count += left
                
        return count