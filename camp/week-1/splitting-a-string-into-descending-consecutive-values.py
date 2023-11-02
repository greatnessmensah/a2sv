class Solution:
    def splitString(self, s: str) -> bool:
        def get_candidates(idx, prev):
            ans = []
            for i in range(idx, len(s)):
                res = s[idx:i+1]
                if (prev-1) == int(res):
                    ans.append([int(res), i+1])
                elif prev == -1 and i != len(s)-1:
                    ans.append([int(res), i+1])
                    
            return ans
 
        
        def search(idx, prev):
            if idx ==len(s):
                return True
                
            for (p, i) in get_candidates(idx, prev):
                if search(i, p):
                    return True
            
            return False
                
        return search(0, -1)
    