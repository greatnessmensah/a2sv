class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, n: int) -> None:
        curr = self.root

        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            if bit not in curr:
                curr[bit] = {}
                
            curr = curr[bit]
            
    def maxxor(self, n) -> int:
        curr = self.root
        ans = 0
        
        for i in range(31, -1, -1):        
            bit = (n >> i) & 1
            if 1-bit in curr:
                ans |= 1 << i
                curr = curr[1-bit]
            else:
                curr = curr[bit]
                
        return ans


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        maxi = 0
        
        for num in nums:
            trie.insert(num)
        
        for num in nums:
            maxi = max(maxi, trie.maxxor(num))
        
        return maxi
        
