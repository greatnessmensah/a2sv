class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyStack:

    def __init__(self):
        self.head = Node()
        

    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> int:
        node = self.head
        var = node.val
        self.head = self.head.next
        
        return var
        
        
    def top(self) -> int:
        node = self.head
            
        return node.val
        
        

    def empty(self) -> bool:
        node = self.head
        
        if node.next:
            return False
        
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()