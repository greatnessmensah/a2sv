class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            if bill == 10:
                ten += 1
                if five < 1:
                    return False
                five -= 1
            if bill == 20:
                if ten < 1:
                    if 5*five >= 15:
                        five -= 3
                        continue
                if five < 1 or ten < 1:
                    return False
                five -= 1
                ten -= 1
                
        return True
