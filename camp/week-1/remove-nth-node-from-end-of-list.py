# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        count = 0
        
        while fast and count < n:
            fast = fast.next
            count += 1
            
        if not fast and head:
            head = head.next
            return head
            
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        if slow.next:
            slow.next = slow.next.next
        
        return head
        
        