class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(num=x, idx=abs(n)):
            if idx == 0:
                return 1
            
            if not idx % 2:
                return pow(num*num, idx//2)
            return num * pow(num*num, (idx-1)//2)
        
        ans = pow()
        
        if n <= 0:
            return 1/ans
        
        return float(ans)