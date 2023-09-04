# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
         
        prev = None
        
        while slow:
            nextt = slow.next
            slow.next = prev
            prev = slow
            slow = nextt
        
        one = prev
        two = head
        
        while one:
            if one.val != two.val:
                return False
            one = one.next
            two = two.next
            
        return True