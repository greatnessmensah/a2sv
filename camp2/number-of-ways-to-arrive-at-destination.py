class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        
        for u, v, t in roads:
            graph[u].append((t, v))
            graph[v].append((t, u))
            
        heap = [[0, 0]]
        nodes = [float(inf)] * n
        heapify(heap)
        mini = 0
        
        while heap:
            time, node = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            
            nodes[node] = time
                 
            for t, nei in graph[node]:
                if nei in visited:
                    continue
                heappush(heap, [time+t, nei])
                    
        mini = nodes[-1]
        visit = set()
        memo = {}
        
        
        def dp(i,cost):
            if i == 0:
                return 1
            
            add = 0
            
            if i not in memo:
                for time, nei in graph[i]:
                    if time + cost + nodes[nei] == mini:
                        add += dp(nei, time+cost)
                memo[i] = add
            
            return memo[i]
        
        
        return dp(n-1, 0) % ((10**9) + 7)
