# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        
        tail = node = ListNode(0, head)
        count = 0
        cnt = 0
        
        while count < left-1:
            node = node.next
            count += 1
            
        new_node = node.next
        
        while cnt < (right-left):
            nextt = new_node.next
            new_node.next = nextt.next
            nextt.next = node.next
            node.next = nextt
            cnt += 1
            
        return tail.next
            
        
        