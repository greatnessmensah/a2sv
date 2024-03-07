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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = DisjointSet()
        
        for eq in equations:
            if "==" in eq:
                uf.union(eq[0], eq[-1])
        
        for eq in equations:
            if "==" in eq:
                if uf.find(eq[0]) != uf.find(eq[-1]):
                    return False
            elif "!=" in eq:
                if uf.find(eq[0]) == uf.find(eq[-1]):
                    return False
                
        return True
