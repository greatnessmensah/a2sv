class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)
        
        while len(stones) > 1:
            first = abs(heappop(stones))
            second = abs(heappop(stones))
            
            if first == second:
                continue
            else:
                second -= first
                heappush(stones, second)
                
        return -stones[0] if len(stones) > 0 else 0
            