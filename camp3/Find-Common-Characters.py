class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word = words[0]
        hashmap = defaultdict(int)
        res = []
        
        for c in word:
            count = float("inf")
            for w in words:
                count = min(count, w.count(c))
            hashmap[c] = count
            
        for key, value in hashmap.items():
            for i in range(value):
                res.append(key)
        
        return res
