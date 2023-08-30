class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        window = defaultdict(int)
        window[0] = 1
        curr = ans = 0
        
        for right in range(len(nums)):
            curr += nums[right]
            mod = curr%k
            ans += window[mod]
            window[mod] += 1
            
        return ans
        