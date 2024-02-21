class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmask = [0] * len(words)
        
        for i in range(len(words)):
            for c in words[i]:
                bitmask[i] |= 1 << (ord(c) - ord('a'))
                
        maxi = 0
                
        for i in range(len(words)):
            for j in range(len(words)):
                if not (bitmask[i] & bitmask[j]):
                    maxi = max(maxi, len(words[i]) * len(words[j]))
        
        return maxi
