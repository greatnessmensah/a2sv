class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        hashmap = defaultdict(list)
        visited = set()
        
        for n in edges:
            hashmap[n[0]].append(n[1])
            hashmap[n[1]].append(n[0])
        
            
        def dfs(vertex, visited):
            if vertex in visited:
                return False
            if vertex == destination:
                return False
            visited.add(vertex)
            
            for neighbour in hashmap[vertex]:
                if dfs(neighbour, visited):
                    return True
                    
        return dfs(source, visited)
