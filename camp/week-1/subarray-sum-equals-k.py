class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        window = defaultdict(int)
        window[0] = 1
        curr = ans = 0
        
        for right in range(len(nums)):
            curr += nums[right]
            ans += window[curr-k]
            window[curr] += 1
            
        return ans
        