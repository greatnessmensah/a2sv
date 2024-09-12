class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = (10 ** 9 + 7)
        
        @lru_cache(100)
        def dp(i, a, l):
            if a >= 2:
                return 0
            
            if l >= 3:
                return 0

            if i == n:
                return 1
            
            ans = 0

            for c in ["L", "P", "A"]:
                if c == "L":
                    ans += dp(i+1, a, l+1)
                elif c == "P":
                    ans += dp(i+1, a, 0)
                else:
                    ans += dp(i+1, a+1, 0)
            return ans % MOD
        
        return dp(0, 0, 0)
