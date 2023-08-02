class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        """
        convert both arrays to set and find intersection
        return minimum common_val else -1.
        """
        common_vals = set(nums1).intersection(nums2)
        if not common_vals:
            return -1
        else:
            return min(common_vals)

"""
Time: O(min(nums1, nums2)) => O(nums1 + nums2)
Space: O(num1 + nums2)
"""
