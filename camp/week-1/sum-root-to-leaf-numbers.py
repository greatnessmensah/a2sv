# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        
        def solve(root, res):
            nonlocal total
            if not root:
                return
            res += str(root.val)
            
            if not root.left and not root.right:
                total += int(res) if res else 0
                
            solve(root.left, res)
            solve(root.right, res)
            
            
        solve(root, "")
        
        return total
