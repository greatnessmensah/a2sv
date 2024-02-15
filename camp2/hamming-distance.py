class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        k = 0
        n = max(x, y).bit_length()
        count = 0
        
        while k <= n:
            if (x & (1 << k) != 0) != (y & (1 << k) != 0):
                count += 1
            k += 1
            
        return count
        
