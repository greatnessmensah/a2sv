class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         graph = graph = {i:[] for i in range(numCourses)}
        res = []

#         for u, v in prerequisites:
#             graph[u].append(v)
            
#         def bfs(src, des, graph):
#             queue = deque([src])
#             visited = set()

#             while queue:
#                 node = queue.popleft()
#                 visited.add(node)

#                 if node == des:
#                     return True

#                 for nei in graph[node]:
#                     if nei not in visited:
#                         queue.append(nei)

#             return False
        
#         for u, v in queries:
#             res.append(bfs(u, v, graph))
            
#         return res

        dist = [[float("inf")] * numCourses for _ in range(numCourses)]
        
        for u, v in prerequisites:
            dist[u][v] = 1
        
        for i in range(numCourses):
            dist[i][i] = 0
            
        for c in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dist[i][j] = min(dist[i][j], dist[i][c]+dist[c][j])

        for u, v in queries:
            res.append(dist[u][v] != float("inf"))
            
        return res
        
