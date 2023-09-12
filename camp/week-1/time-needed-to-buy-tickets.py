class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        
        while tickets[k] > 0:
            for left in range(len(tickets)):
                if tickets[k]==0:
                    return time
                if tickets[left] > 0:
                    tickets[left] -= 1
                    time += 1
                
        return time