class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        same = -1
        k = n.bit_length()
        
        for i in range(k):
            if n & (1 << i) != 0:
                check = 1
            else:
                check = 0
            if same == check:
                return False
            same = check
            
        return True
        
