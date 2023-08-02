class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        left and right pointer moves when greater or less
        else return -1
        """
        left = right = 0
        
        while left < len(nums1) and right <len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] > nums2[right]:
                right += 1
            else: 
                return nums1[left]
            
        return -1
        

"""
Time: O(nums1 + nums2)
Space: O(1)
"""
