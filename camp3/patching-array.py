class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        mini = 1
        i = ans = 0
        
        while mini <= n:
            if i < len(nums) and nums[i] <= mini:
                mini += nums[i]
                i += 1
            else:
                mini += mini
                ans += 1
                
        return ans
