class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)
        lo = 1
        
        def speed(num, hours):
            time = 0
            
            for i in range(len(piles)):
                time += ceil(piles[i]/num)
                
                if time > hours:
                    return False
                
            return True

        while lo <= hi:
            mid = lo + (hi-lo) // 2
            
            if speed(mid, h):
                hi = mid - 1
            else:
                lo = mid + 1
                
        return lo
        