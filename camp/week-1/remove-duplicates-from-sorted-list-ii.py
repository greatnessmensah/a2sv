# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        hashmap = defaultdict(int)
        new = ListNode()
        node = head
        curr = head
        
        while node:
            hashmap[node.val] += 1
            node = node.next
            
        while curr and curr.next:
            if hashmap[curr.next.val] > 1:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        if hashmap[head.val] > 1:
            head = head.next
            
        return head
        