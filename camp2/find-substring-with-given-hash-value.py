class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        res = 0
        left = 0
        hash_s = 0
        s = s[::-1]
        ans = ""
        
        def val(c):
            return ord(c)-ord("a") + 1

        for i in range(k):
            ex = k-1-i
            hash_s += (val(s[i]) * pow(power, ex, modulo))
            hash_s %= modulo
            
        if hash_s == hashValue:
            ans = s[left:i+1][::-1]
        
        for right in range(k, len(s)):
            hash_s *= power
            hash_s %= modulo
            hash_s += (val(s[right])) % modulo
            hash_s -= (val(s[left]) * pow(power, k, modulo))
            hash_s %= modulo
            left += 1
            
            if hash_s == hashValue:
                ans = s[left:right+1][::-1]
                
        return ans
