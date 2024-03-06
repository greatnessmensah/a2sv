class DisjointSet:
    def __init__(self):
        self.root = {chr(ord("a")+i): chr(ord("a")+i) for i in range(26)}
        
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
            if rootV < rootU:
                self.root[rootU] = rootV
            else:
                self.root[rootV] = rootU


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(baseStr)
        uf = DisjointSet()
        
        for i in range(len(s1)):
            uf.union(s1[i], s2[i])
            
        return "".join(uf.find(c) for c in baseStr)
