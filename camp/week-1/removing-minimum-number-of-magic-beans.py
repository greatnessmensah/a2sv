class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total = sum(beans)
        res = float("inf")
        
        for i in range(len(beans)):
            # prods.append(total - (beans[i]*(len(beans)-i)))
            res = min(res, total - (beans[i]*(len(beans)-i)))
        
        return res
        