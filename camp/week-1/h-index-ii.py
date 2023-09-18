class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lo = 0
        hi = len(citations)-1
        b_index = -1
        
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            
            if citations[mid] < len(citations)-mid:
                lo = mid + 1
            else:
                hi = mid - 1
                b_index = mid
        
        return len(citations) - b_index if b_index > -1 else 0