class DisjointSet:
    def __init__(self, size: int):
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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = DisjointSet(n)
        
        for edge in edges:
            uf.union(edge[0], edge[1])
            
        return uf.find(source) == uf.find(destination)
