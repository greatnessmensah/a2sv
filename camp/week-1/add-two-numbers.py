# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = l1
        right = l2
        total = tail = ListNode()
        carry = 0
        
        while left or right:
            summ = ListNode()
            add = 0
            if left:
                add += left.val
                left = left.next
            if right:
                add += right.val
                right = right.next
            add += carry
            if add >= 10:
                summ.val = add%10
                carry = 1
            else:
                summ.val = add
                carry = 0
            tail.next = summ  
            tail = tail.next
            
        if carry > 0:
            car = ListNode(carry)
            tail.next = car
            
        return total.next