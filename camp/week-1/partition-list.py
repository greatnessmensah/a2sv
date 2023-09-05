# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        
        less = l_node = ListNode()
        great = g_node = ListNode()
        node = head
        
        while node:
            if node.val < x:
                l_node.next = node
                l_node = l_node.next
            else:
                g_node.next = node
                g_node = g_node.next
                
            node = node.next
            
        g_node.next = None
        l_node.next = great.next
        
        return less.next
        