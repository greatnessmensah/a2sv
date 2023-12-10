class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        groups = [-1] * (n + 1)

        def dfs(node, group):
            groups[node] = group

            for neighbor in graph[node]:
                if groups[neighbor] == group:
                    return False
                if groups[neighbor] == -1: 
                    if not dfs(neighbor, 1 - group):
                        return False
                    
            return True
        
        for i in range(1, n + 1):
            if groups[i] == -1:
                if not dfs(i, 0):
                    return False
                
        return True
