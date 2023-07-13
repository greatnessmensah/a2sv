class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        
        while l <= r:
            summed = numbers[l] + numbers[r]
            
            if summed < target:
                l += 1
            elif summed > target:
                r -= 1
            else:  
                return [l+1, r+1]

"""
Time: O(N)
Space:(1)
"""
