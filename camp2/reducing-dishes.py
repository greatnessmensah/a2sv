class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        maxi = 0
        
        for i in range(len(satisfaction)):
            summ = 0
            k = 1
            for j in range(i, len(satisfaction)):
                summ += (satisfaction[j] * k)
                k += 1
            if satisfaction[0] >=0 : 
                return summ
                
            maxi = max(summ, maxi)
            
        return maxi
