# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        first = head
        maxi = 0
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        
        while slow:
            nextt = slow.next
            slow.next = prev
            prev = slow
            slow = nextt
            
            
        while first and prev:
            maxi = max(maxi, first.val+prev.val)
            prev = prev.next
            first = first.next
            
        return maxi