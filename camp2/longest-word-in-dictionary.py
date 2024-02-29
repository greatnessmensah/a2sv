class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.is_end = True
    

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        res = ""
        
        for c in words:
            trie.insert(c)
        
        for word in words:
            if len(word) < len(res): 
                continue
            
            curr = trie.root
            
            for c in word:
                curr = curr.children[c]
                if not curr.is_end: 
                    break
            
            if curr.is_end and (len(word) > len(res) or (len(word) == len(res) and word < res)):
                res = word        
            
        return res
                
            
        
