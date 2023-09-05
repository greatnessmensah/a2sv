# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        
        odds = o_tail = ListNode()
        evens = e_tail = ListNode()
        node = head
        count = 0
        
        while node:
            if count % 2 == 0:
                e_tail.next = node
                e_tail = e_tail.next
            else:
                o_tail.next = node
                o_tail = o_tail.next
                
            count += 1
            node = node.next
            
        o_tail.next = None
        e_tail.next = odds.next
        
        return evens.next
