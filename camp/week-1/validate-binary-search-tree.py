# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def solve(root, left, right):
            if not root:
                return True
            
            if  root.val >= right or root.val <= left:
                return False
            
            first = solve(root.left, left, root.val)
            second = solve(root.right, root.val, right)
            
            return first and second

        return solve(root, float("-inf"), float("inf"))