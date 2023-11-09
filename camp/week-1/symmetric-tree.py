# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right
        
        def solve(first, second):
            if not first and not second:
                return True
            elif not first or not second:
                return False
            elif first.val != second.val:
                return False

            return solve(first.left,second.right) and solve(first.right,second.left)
        
        return solve(left, right)
            