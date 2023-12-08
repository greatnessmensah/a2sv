# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        arr = []
        
        while queue:
            level = len(queue)
            count = 0
            
            for _ in range(level):
                node = queue.popleft()
                count += node.val
                
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                    
            arr.append(count / level)
        return arr
        
        
