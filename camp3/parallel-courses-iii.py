class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        edges = defaultdict(int)
        graph = {i: [] for i in range(1, n+1)}
        ans = 0
        
        for a, b in relations:
            graph[a].append(b)
            edges[b] += 1
            
        queue = deque([key for key in graph.keys() if edges[key] == 0])
        dp = [0] + time
        
        while queue:
            l = len(queue)
            
            for _ in range(l):
                node = queue.popleft()
                for nei in graph[node]:
                    dp[nei] = max(dp[nei], dp[node]+time[nei-1])
                    edges[nei] -= 1
                    
                    if edges[nei] == 0:
                        queue.append(nei)
            
        return max(dp)
