class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)
        
        def capacity(num, d):
            cap = 0
            needed = 1
            
            for i in range(len(weights)):
                if cap+weights[i] > num:
                    needed += 1
                    cap = 0
                cap += weights[i]
                    
            return needed <= d
        
        while lo < hi:
            mid = lo + (hi-lo) // 2
            
            if capacity(mid,days):
                hi = mid
            else:
                lo = mid + 1
                
        return lo