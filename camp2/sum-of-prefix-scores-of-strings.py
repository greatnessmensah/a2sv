class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.count += 1
            
    def prefixsum(self, prefix: str) -> int:
        curr = self.root
        res = 0

        for p in prefix:
            # if p not in prefix:
            #     return 0
            curr = curr.children[p]
            res += curr.count

        return res
    
        
class TrieNode:
    def __init__(self):
        # self.children = {}
        self.children = defaultdict(TrieNode)
        self.count = 0


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        ans = []
        
        for word in words:
            trie.insert(word)
            
        for prefix in words:
            ans.append(trie.prefixsum(prefix))
            
        return ans
        
