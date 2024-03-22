class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
#         right = len(needle)
        
#         for left in range(len(haystack)):
#             if haystack[left:right] == needle:
#                 return left
#             else:
#                 right += 1
                
#         return -1

        
#         for left in range(len(haystack)-len(needle)+1):
#             ans = left
#             right = 0
#             while haystack[left] == needle[right]:
#                 left += 1
#                 right += 1
                
#                 if right == len(needle):
#                     return ans
                
#             right = 0
            
#         return -1
                
        MOD = 10**9 + 7
        alpha = {c: idx+1 for idx, c in enumerate(string.ascii_lowercase)}
        res = 0
        left = 0
        
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(needle)):
            ex = len(needle)-1-i
            res += (alpha[needle[i]] * (31**ex)) % MOD
            res %= MOD

        count = 0
        for i in range(len(needle)):
            ex = len(needle) - 1 - i
            count += (alpha[haystack[i]] * (31**ex)) % MOD
            count %= MOD

        if count == res:
            return 0

        for right in range(len(needle), len(haystack)):
            count *= 31
            count += (alpha[haystack[right]]) % MOD
            count -= (alpha[haystack[left]] * (31**len(needle))) % MOD
            count %= MOD
            left += 1
            
            if count == res:
                return left

        return -1
