class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        sieve = [True] * (n + 1)
        count = 0
        prime = []
        
        for num in range(2, n):
            if sieve[num]:
                count += 1
                prime.append(num)
                
                for multiples in range(num * num, n + 1, num):
                    sieve[multiples] = False
                    
        return count
