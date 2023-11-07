# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        first = p
        second = q
        
        if not first and not second:
            return True
        elif not first or not second:
            return False
        elif first.val != second.val:
            return False
        
        return self.isSameTree(first.left,second.left) and self.isSameTree(first.right,second.right)