class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        first = float("-inf")
        second = float("-inf")
        idx_one = -1
        idx_two = -1
        
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                first = arr[i-1]
                idx_one = i - 1
        
        if idx_one == -1:
            return arr
        
        idx_two = idx_one + 1
        
        for i in range(idx_one+1, len(arr)):
            if arr[i] < first and arr[i] > arr[idx_two]:
                idx_two = i 
                
        arr[idx_one], arr[idx_two] = arr[idx_two], arr[idx_one]
        
        return arr
