class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        nodes = {i: [] for i in range(len(graph))}
        edges = defaultdict(int)
        res = []
        
        for key in nodes.keys():
            for val in graph[key]:
                nodes[val].append(key)
            edges[key] += len(graph[key])
            
        queue = deque([key for key, val in edges.items() if val == 0])
        
        print(nodes)
        print(edges)
        print(queue)

        while queue:
            node = queue.popleft()

            for nei in nodes[node]:
                edges[nei] -= 1
                if edges[nei] == 0:
                    queue.append(nei)
                    del edges[nei]

            res.append(node)
            
        return sorted(res)
        
        
