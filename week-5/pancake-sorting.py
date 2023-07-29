class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        res = []
        
        for i in range(n):
            max_elem = max(arr[:n - i])
            max_idx = arr.index(max_elem) + 1
            arr[:max_idx] = reversed(arr[:max_idx])
            res.append(max_idx)
            
            arr[:n - i] = reversed(arr[:n - i])
            res.append(n - i)
            
        return res
        