class Node:
    def __init__(self,val=None):
        self.left = None
        self.right = None
        self.val = val

class MyCircularDeque:
    def __init__(self, k: int):
        self.max = k
        self.cnt = 0
        self.head = Node()
        self.tail = self.head
    
    def insertFront(self,value):
        if(self.cnt < self.max):
            right = self.head
            self.head.left = Node(value)
            self.head = self.head.left
            self.head.right = right
            self.cnt += 1
            return True
        else:
            return False
    
    def insertLast(self,value):
        if(self.cnt < self.max):
            self.tail.val = value
            left = self.tail
            self.tail.right = Node()
            self.tail = self.tail.right
            self.tail.left = left 
            print(self.tail.left.val)
            self.cnt += 1
            return True
        else:
            return False
    
    def deleteFront(self):
        if(self.cnt > 0):
            self.head = self.head.right
            self.cnt -= 1
            return True
        else:
            return False
    
    def deleteLast(self):
        if(self.cnt > 0):
            self.tail = self.tail.left
            self.tail.val = None
            self.cnt -= 1
            return True
        else:
            return False
    
    def getFront(self):
        return self.head.val if self.cnt > 0 else -1
    
    def getRear(self):
        return self.tail.left.val if self.cnt > 0 else -1
    
    def isEmpty(self):
        return self.cnt == 0
    
    def isFull(self):
        return self.cnt == self.max
    

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