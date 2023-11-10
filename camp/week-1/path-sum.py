# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        count = 0
        
        def solve(root, count):
            if not root:
                return False
            
            count += root.val
            
            if not root.left and not root.right and count == targetSum:
                return True
            
            left = solve(root.left, count)
            right = solve(root.right, count)
            
            return left or right
        
        return solve(root, count)