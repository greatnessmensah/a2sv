class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:  
        sorted_nums = sorted(nums)
        return [i for i in range(len(sorted_nums)) if sorted_nums[i] == target]

"""
Time: O(NlogN)
Space: O(N)
"""
