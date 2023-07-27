class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        target = Counter(p)
        window = Counter(s[:len(p)-1])
        
        for i in range(len(p)-1, len(s)):
            window[s[i]] += 1
            
            if window == target:
                res.append(i-len(p)+1)
            window[s[i-len(p)+1]] -= 1
            
            if s[i-len(p)+1] == 0:
                del s[i-len(p)+1]
                
        return res