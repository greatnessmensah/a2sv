class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        counter = 0
        node = self.head
        
        while node:
            if counter == index:
                return node.value
            node = node.next
            counter += 1
        return -1
        
    
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        node = self.head
        counter = 0
        
        if not node:
            new_node.next = self.head
            self.head = new_node
            return
            
        while node and node.next:
            node = node.next
            counter += 1

        node.next = new_node
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return
        counter = 0
        new_node = Node(val)
        node = self.head
        
        while node:
            if counter == index-1:
                new_node.next = node.next
                node.next = new_node
            node = node.next
            counter += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
                
        counter = 0
        node = self.head
        
        while node:
            if counter == index-1 and node.next:
                node.next = node.next.next
            node = node.next
            counter += 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)