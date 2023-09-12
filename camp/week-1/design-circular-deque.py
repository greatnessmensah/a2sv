class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = ListNode()
        self.tail = self.queue
        self.head = self.queue
        self.k = k
        self.count = 0
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            new_node = ListNode(value)
            self.queue.next = new_node
            self.tail = self.queue.next
            self.head = self.queue.next
            self.count += 1
        else:
            new_node = ListNode(value)
            self.queue.next = new_node
            new_node.next = self.head
            self.head = self.queue.next
            self.count += 1
        
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            new_node = ListNode(value)
            self.queue.next = new_node
            self.tail = self.queue.next
            self.head = self.queue.next
            self.count += 1
        else:
            new_node = ListNode(value)
            self.tail.next = new_node
            self.tail = self.tail.next;
            self.count += 1
        
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        elif self.head == self.tail:
            self.head = self.queue
            self.tail = self.queue
            self.count -= 1
        else:
            self.queue.next = self.head.next
            self.head = self.queue.next
            self.count -= 1
            
        return True
    

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        elif self.head == self.tail:
            self.head = self.queue
            self.tail = self.queue
            self.count -= 1
        else:
            temp = self.queue
            while temp.next != self.tail:
                temp = temp.next
        
            self.tail = temp
            self.tail.next = None
            self.count -= 1
            
        return True

    def getFront(self) -> int:
        if not self.head:
            return -1
        
        return self.head.val
        

    def getRear(self) -> int:
        if not self.tail:
            return -1
        
        return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()