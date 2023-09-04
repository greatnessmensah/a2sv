# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = list1
        second = list2
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
        