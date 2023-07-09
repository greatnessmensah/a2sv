class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        res = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                sum = 0
                for r in range(max(0, i - k), min(n, i + k + 1)):
                    for c in range(max(0, j - k), min(m, j + k + 1)):
                        sum += mat[r][c]
                res[i][j] = sum
                
        return res


"""
Time: O(k^2(N*M))
Space: O(N*M)
"""
