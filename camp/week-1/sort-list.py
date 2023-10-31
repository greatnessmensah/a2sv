# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left, right):
            first = left
            second = right
            new_node = ListNode(0)
            tail = new_node

            while first and second:
                if first.val < second.val:
                    tail.next = first
                    first = first.next
                else:
                    tail.next = second
                    second = second.next  

                tail = tail.next

            if first:
                tail.next = first

            if second:
                tail.next = second
                
            return new_node.next

        def split(head):
            if not head or not head.next:
                return head
            
            fast = head
            slow = head
            check = head
            
            while fast and fast.next:
                fast = fast.next.next
                check = slow
                slow = slow.next
                
            check.next = None
                
            return merge(split(head), split(slow))
        
        
        return split(head)
                
        
                
                
            
            
            