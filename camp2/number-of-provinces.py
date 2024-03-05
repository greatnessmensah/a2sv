class DisjointSet:
    def __init__(self, n: int):
        self.root = {i: i for i in range(n)}
        self.size = [1] * n
        
    def find(self, node: int) -> int:
        while node != self.root[node]:
            node = self.root[node]
            
        return node
    
    def union(self, u, v) -> None:
        rootV = self.find(v)
        rootU = self.find(u)
        
        if rootV != rootU:
            if self.size[rootV] > self.size[rootU]:
                self.root[rootU] = rootV
                self.size[rootV] += self.size[rootU]
            else:
                self.root[rootV] = rootU
                self.size[rootU] += self.size[rootV]

                
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = DisjointSet(n)
        count = 0
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and uf.find(i) != uf.find(j):
                    uf.union(i, j)
                    count += 1
                
        return n - count
