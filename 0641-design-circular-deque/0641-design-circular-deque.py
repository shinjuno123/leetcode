class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.len = 0
        self.head = Node()
        self.tail = Node()
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self,node, new_node):
        prev = node.right
        node.right = new_node
        new_node.left = node
        new_node.right = prev
        prev.left = new_node
    
    def _delete(self,node):
        next = node.right.right
        node.right = next
        next.left = node
    
    def insertFront(self, value: int) -> bool:
        if self.k > self.len:
            self._add(self.head,Node(value))
            self.len += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.k > self.len:
            self._add(self.tail.left,Node(value))
            self.len += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.len > 0:
            self._delete(self.head)
            self.len -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.len > 0:
            self._delete(self.tail.left.left)
            self.len -= 1
            return True
        else:
            return False
        
    def getFront(self) -> int:
        return self.head.right.value if self.len > 0 else -1 

    def getRear(self) -> int:
        return self.tail.left.value if self.len > 0 else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k


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