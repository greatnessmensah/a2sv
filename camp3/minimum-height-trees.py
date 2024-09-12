class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(n)}
        edge = defaultdict(int)
        
        if n == 1:
            return [0]
        
        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)
            edge[u] += 1
            edge[v] += 1
            
        queue = deque([key for key, nodes in edge.items() if nodes == 1 ])
        
        while n > 2:
            n -= len(queue)
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                for nei in graph[node]:
                    edge[nei] -= 1
                    if edge[nei] == 1:
                        queue.append(nei)  
                        del edge[nei]
                
        return list(queue)
                
        
        
