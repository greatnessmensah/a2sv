class Solution:
    def countPrimes(self, n: int) -> int:
        checks = [False] * (n)
        i = 2

        while i <int(n**(1/2))+1:
            if not checks[i]:
                for j in range(i+i, n, i):
                    checks[j] = True
            i += 1
        
        return checks[2:].count(False)
