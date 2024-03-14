# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         curr = head
#         prev = None
        
#         while curr:
#             nextt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nextt
            
#         return prev
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None

        curr = head
        
        if head.next:
            curr = self.reverseList(head.next)
            head.next.next = head
        head.next = None    

        return curr     
