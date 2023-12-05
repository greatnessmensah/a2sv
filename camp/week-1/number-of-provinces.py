class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        hashmap = {i+1:[] for i in range(len(isConnected))}
        visited = set()
        count = 0 
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i != j:
                    hashmap[i+1].append(j+1)
                    
        def dfs(node):
            visited.add(node)
            for prov in hashmap[node]:
                if prov not in visited:
                    dfs(prov)
      
        for key in hashmap.keys():
            if key not in visited:
                dfs(key)
                count += 1
                
        return count
        
