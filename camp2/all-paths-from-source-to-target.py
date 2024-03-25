class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)
        visited = set()
        
        def dfs(node, res):
            res.append(node)
            visited.add(node)
            if node == n-1:
                ans.append(res.copy())
            
            for nei in graph[node]:
                dfs(nei, res)
                
            res.pop()
            visited.remove(node)
            
        dfs(0, [])
        
        return ans
