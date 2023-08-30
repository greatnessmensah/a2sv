class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        row = len(self.matrix)
        col = len(self.matrix[0])
        self.p_matrix = [[0]*(col+1) for i in range((row+1))]
        
        for i in range(1, len(self.p_matrix)):
            rows = len(self.p_matrix[0])
            for r in range(1, rows):
                self.p_matrix[i][r] = self.p_matrix[i][r-1] + self.matrix[i-1][r-1]
                
        for i in range(len(self.p_matrix[0])):
            for j in range(1, len(self.p_matrix)):
                self.p_matrix[j][i] = self.p_matrix[j-1][i] + self.p_matrix[j][i]
                
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
            summ = self.p_matrix[row2+1][col2+1] - self.p_matrix[row2+1][col1] - self.p_matrix[row1][col2+1] + self.p_matrix[row1][col1]
            
            return summ
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)