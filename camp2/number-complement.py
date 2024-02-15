class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        i = 1
        
        while i < num:
            if i & num == 0:
                ans += i
            i = i << 1
            
        return ans
          
