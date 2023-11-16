class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = defaultdict(int)
        
        for word in words:
            hashmap[word] += 1
        
        max_heap = [[-freq, num] for num, freq in hashmap.items()]
        heapify(max_heap)
        res = []
        
        for i in range(k):
            _, word = heappop(max_heap)
            res.append(word)
            
        return res

        