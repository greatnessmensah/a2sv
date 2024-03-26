class Solution:
    def longestPrefix(self, s: str) -> str:
#         n = len(s)
#         a = 31 ** (n-1)
#         MOD = 10**9 + 7
#         pref_s = 0
#         suf_s = 0
#         left, right = 0, n-1
#         alpha = {c: idx+1 for idx, c in enumerate(string.ascii_lowercase)}
#         p = 1
#         ans = float("inf")
        
#         while left < n-1:
#             pref_s *= 31
#             pref_s += (alpha[s[left]])
#             pref_s %= MOD
            
#             suf_s += alpha[s[right]] * p
#             suf_s %= MOD
#             p *= 31
#             p %= MOD
            
#             if pref_s == suf_s:
#                 ans = left
                
#             left += 1
#             right -= 1
            
#         return s[:ans+1] if ans != float("inf") else ""

        n = len(s)
        lps = [0] * n
        
        for i in range(1, n):
            j = lps[i-1]
            
            while j > 0 and s[j] != s[i]:
                j = lps[j-1]
                
            if s[j] == s[i]:
                j += 1
                
            lps[i] = j
        
        return s[:lps[-1]]
        
            
    
        
