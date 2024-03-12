class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         graph = defaultdict(list)

#         for u, v, w in times:
#             graph[u].append((w, v))
            
#         heap = [[0, k]]
#         heapify(heap)
#         visited = set()
        
#         while heap:
#             weight, node = heappop(heap)
#             visited.add(node)
            
#             if len(visited) == n:
#                 return weight
                
#             for wei, nei in graph[node]:
#                 if nei not in visited:
#                     heappush(heap, [weight+wei, nei])
                    
#         return -1

        dist = [[float("inf")] * n for _ in range(n)]
    
        for u, v, w in times:
            dist[u-1][v-1] = w
        
        for i in range(n):
            dist[i][i] = 0
            
        for c in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][c]+dist[c][j])
                    
        return max(dist[k-1]) if max(dist[k-1]) != float("inf") else -1
