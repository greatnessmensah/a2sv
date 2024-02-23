# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(int)
        
        def dp(node):
            if node in memo:
                return memo[node]
            
            if not node:
                return [0, 0]
            
            left = dp(node.left)
            right = dp(node.right)
            
            
            one = node.val + left[1] + right[1]
            two = max(left) + max(right)
            
            memo[node] = [one, two]
            
            return memo[node]
        
        return max(dp(root))
