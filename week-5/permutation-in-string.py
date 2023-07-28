class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        window = Counter(s2[:len(s1)-1])
        left = 0
        
        if window == target:
            return True
        
        for right in range(len(s1)-1, len(s2)):
            window[s2[right]] += 1
            
            if window == target:
                return True
            window[s2[left]] -= 1
            
            if window[s2[left]] == 0:
                del window[s2[left]]
                
            left += 1
        
        return False