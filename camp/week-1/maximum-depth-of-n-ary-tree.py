"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        arr = float("-inf")
        if not root:
            return 0
        if not root.children:
            return 1
        
        for i in root.children:
            arr = max(arr, 1 + self.maxDepth(i))
        
        return arr
            
            
                
