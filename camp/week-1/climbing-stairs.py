hashmap = {}
class Solution:
    def climbStairs(self, n: int) -> int:
#         fib = [1, 1]
        
#         for i in range(1, n+1):
#             fib.append(fib[-2]+fib[-1])

#         return fib[n]
        
        if n < 2:
            return 1
        if n in hashmap:
            return hashmap[n]
        else:
            hashmap[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
            
        return self.climbStairs(n-2) + self.climbStairs(n-1)