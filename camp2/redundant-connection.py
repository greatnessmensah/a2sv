class DisjointSet:
    def __init__(self, size):
        self.root = {i: i for i in range(size)}
        self.size = [1] * size
        
    def find(self, node: int) -> int:
        root = node
        
        while root != self.root[root]:
            root = self.root[root]
            
        while node != root:
            parent = self.root[node]
            self.root[node] = root
            node = parent
            
        return root
    
    def union(self, u: int, v: int) -> None:
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = DisjointSet(n)
        
        for u, v in edges:
            if uf.find(u-1) != uf.find(v-1):
                uf.union(u-1, v-1)
            elif uf.find(u-1) == uf.find(v-1):
                return [u, v]
            
        return []
