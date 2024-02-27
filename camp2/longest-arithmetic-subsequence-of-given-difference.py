class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        
        for i in range(len(arr)):
            if arr[i] - difference in dp:
                dp[arr[i]] = 1 + dp[arr[i]-difference]
            else:
                dp[arr[i]] = 1
        
        return max(dp.values())
