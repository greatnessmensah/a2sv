class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashmap = defaultdict(list)
        
        for n in edges:
            hashmap[n[0]].append(n[1])
            if len(hashmap[n[0]]) > 1:
                return n[0]
            hashmap[n[1]].append(n[0])
            if len(hashmap[n[1]]) > 1:
                return n[1]
            
            
        