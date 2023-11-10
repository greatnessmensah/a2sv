# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def solve(root, val):
            if root.left and not root.right:
                if root.val < val:
                    root.right = TreeNode(val)
                    return
                else:
                    return self.insertIntoBST(root.left, val)
            if root.right and not root.left:
                if root.val > val:
                    root.left = TreeNode(val)
                    return
                else:
                    return self.insertIntoBST(root.right, val)
            if not root.left and not root.right:
                if root.val < val:
                    root.right = TreeNode(val)
                    return
                else:
                    root.left = TreeNode(val)
                    return
        
            if root.val < val:
                return self.insertIntoBST(root.right, val)
            else:
                return self.insertIntoBST(root.left, val)
            
        solve(root, val)
        
        return root
            
            