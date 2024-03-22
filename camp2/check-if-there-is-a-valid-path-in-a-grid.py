class UnionFind:
    def __init__(self, size):
        self.root = {}
        self.size = {}

        for i in range(len(size)):
            for j in range(len(size[0])):
                self.root[(i,j)] = (i,j)
                self.size[(i,j)] = 1

    def find(self, node):
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
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        uf = UnionFind(grid)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if inbound(i, j-1) and (grid[i][j-1] in (1, 4, 6)):
                        uf.union((i, j-1), (i, j))
                    if inbound(i, j+1) and (grid[i][j+1] in (1, 3, 5)):
                        uf.union((i, j), (i, j+1))

                elif grid[i][j] == 2:
                    if inbound(i-1, j) and (grid[i-1][j] in (2, 3, 4)):
                        uf.union((i-1, j), (i, j))
                    if inbound(i+1, j) and grid[i+1][j] in (2, 5, 6):
                        uf.union((i, j), (i+1, j))

                elif grid[i][j] == 3:
                    if inbound(i, j-1) and (grid[i][j-1] in (1, 4, 6)):
                        uf.union((i, j-1), (i, j))
                    if inbound(i+1, j) and (grid[i+1][j] in (2, 5, 6)):
                        uf.union((i, j), (i+1, j))

                elif grid[i][j] == 4:
                    if inbound(i, j+1) and (grid[i][j+1] in (1, 3, 5)):
                        uf.union((i, j+1), (i, j))
                    if inbound(i+1, j) and (grid[i+1][j] in (2, 5, 6)):
                        uf.union((i, j), (i+1, j))

                elif grid[i][j] == 5:
                    if inbound(i, j-1) and (grid[i][j-1] in (1, 4, 6)):
                        uf.union((i, j-1), (i, j))
                    if inbound(i-1, j) and (grid[i-1][j] in (2, 3, 4)):
                        uf.union((i, j), (i-1, j))

                else:
                    if inbound(i, j+1) and (grid[i][j+1] in (1, 3, 5)):
                        uf.union((i, j+1), (i, j))
                    if inbound(i-1, j) and (grid[i-1][j] in (2, 3, 4)):
                        uf.union((i, j), (i-1, j))

        return uf.find((0, 0)) == uf.find((n-1, m-1))
