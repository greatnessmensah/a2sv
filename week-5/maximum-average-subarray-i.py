class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi = float("-inf")
        window = sum(nums[:k])
        maxi = window
        
        for i in range(k, len(nums)):
            window += nums[i] - nums[i-k]
            print(window)
            maxi = max(maxi, window)
            
        return maxi/k
        
        