class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        middle_row = rows // 2
        middle_col = cols // 2
        
        upper_diagonal = [mat[i][i] for i in range(min(rows, cols))]
        lower_diagonal = [mat[i][cols-1-i] for i in range(min(rows, cols))]
        middle_element = mat[middle_row][middle_col]
        
        if rows % 2 != 0:
            return (sum(upper_diagonal) + sum(lower_diagonal)) - middle_element
        else:
            return (sum(upper_diagonal) + sum(lower_diagonal))
