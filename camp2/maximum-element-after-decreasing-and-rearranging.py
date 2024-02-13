class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        mini = 1
        
        for i in range(len(arr)):
            if arr[i] >= mini:
                arr[i] = mini
                mini += 1

        return arr[-1]
        
