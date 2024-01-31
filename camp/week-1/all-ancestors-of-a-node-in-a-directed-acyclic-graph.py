class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        nodes = {i: [] for i in range(n)}
        indegrees = defaultdict(int)
        
        for first, second in edges:
            nodes[first].append(second)
            indegrees[second] += 1
            
        queue = deque([i for i in range(n) if i not in indegrees])
        ans = [set() for _ in range(n)]
        
        while queue:
            node = queue.popleft()
            
            for nei in nodes[node]:
                for a in ans[node]:
                    ans[nei].add(a)
                ans[nei].add(node)
                
                indegrees[nei] -= 1
                
                if indegrees[nei] == 0:
                    queue.append(nei)
                    
        return [sorted(list(a)) for a in ans]
