class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(node,idx):
            curr = node
            for i in range(idx,len(word)):
                c = word[i]
                if c is '.': 
                    for child in curr.children.values():
                        if dfs(child,i+1):
                            return True
                    return False
                if c in curr.children:
                    curr = curr.children[c]
                else:
                    return False
            return curr.is_end
        
        return dfs(self.root,0)
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
