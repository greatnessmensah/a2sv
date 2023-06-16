class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) -1
        row_containing_element = None
        
        while l <= r:
            mid = (l+r) // 2
            
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row_containing_element = matrix[mid]
                break
            elif target > matrix[mid][0]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
        
        if not row_containing_element:
            return False
        
        left, right = 0, len(row_containing_element)
                
        while left <= right:
            mid = (left + right) // 2
            if row_containing_element[mid] == target:
                return True
            elif row_containing_element[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
    
    
#         new = []
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 new.append(matrix[i][j])
                
#         return True if target in new else False


        """
        Time: O(log(M*N))
        Space: O(1)
        """
