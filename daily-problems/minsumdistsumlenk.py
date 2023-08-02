class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        set our maxi to 0 and left pointer
        we count the first k elements of nums, if they are disticnt we update maxi with their sum.
        we start adding the following elements from k to len(nums)
        we add elements and decrease the value of the elements by their left pointer
        if value of element is 0 we remove
        we compute the sum of a current window stored in summed
        """
        maxi = 0
        left = 0
        summed = 0
        window = defaultdict(int)
        
        for idx in range(k):
            window[nums[idx]] += 1
            summed += nums[idx]
        
        if len(window) == k:
            maxi = max(maxi, summed)
        
        for right in range(k, len(nums)):
            window[nums[right]] += 1
            window[nums[left]] -= 1
            
            if window[nums[left]] == 0:
                del window[nums[left]]
                
            summed += nums[right]
            summed -= nums[left]
            
            if len(window) == k:
                maxi = max(maxi, summed)
                
            left += 1

        return maxi
    
