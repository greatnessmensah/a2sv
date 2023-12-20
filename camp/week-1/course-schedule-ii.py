class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        edges = defaultdict(int)
        res = []
        
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
            
        for node in graph.keys():
            for val in graph[node]:
                edges[val] += 1
            
        queue = deque([key for key in graph if key not in edges])
        
        while queue:
            course = queue.popleft()
            
            for nei in graph[course]:
                edges[nei] -= 1
                if edges[nei] == 0:
                    queue.append(nei)
                    del edges[nei]
                        
            res.append(course)
            
        return res if len(res) == numCourses else []
            
