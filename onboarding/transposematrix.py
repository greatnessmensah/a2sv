class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        transposed = []
        
        for c in range(cols):
            row = []
            for r in range(rows):
                row.append(matrix[r][c])
            transposed.append(row)

        return transposed
    
        """
        TimeL O(N*M)
        Space: O(N*M))
        """
