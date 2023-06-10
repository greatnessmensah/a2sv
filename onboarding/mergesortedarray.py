class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l, r = 0, 0
        
        while l < len(nums1) and r < len(nums2):
            if nums1[l] != 0:
                l += 1
            else:
                nums1[l] = nums2[r]
                r += 1
                l += 1
                
        nums1.sort()
        
        
