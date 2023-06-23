class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        arr = [[0 for _ in range(c)] for _ in range(r)]
        row = 0
        col = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arr[row][col] = mat[i][j]
                col += 1
                if col == c:
                    col = 0
                    row += 1
        
        return arr

        """
        Time: O(N*M)
        Space: O(N*M)
        """
