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

        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        curr = trie.root
        res = ""
        
        for c in strs:
            trie.insert(c)
        
        while curr:
            if len(curr.children) > 1 or curr.is_end:
                return res
            
            key = list(curr.children)[0]
            res += key
            
            curr = curr.children[key]
            
        return res
        
