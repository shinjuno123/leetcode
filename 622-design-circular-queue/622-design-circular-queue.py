class MyCircularQueue:

    def __init__(self, k: int):
        self.cqueue = [None] * k
        self.k = k
        self.front = 0
        self.rear = 0
    
    def enQueue(self,value:int):
        # if there is space
        if self.cqueue[self.rear] is None:
            self.cqueue[self.rear] = value
            self.rear = (self.rear + 1) % self.k
            return True
        # if there is no space to fill
        else:
            return False
        
    def deQueue(self):
        if self.cqueue[self.front] is None:
            return False
        else:
            v = self.cqueue[self.rear]
            self.cqueue[self.front] = None
            self.front = (self.front + 1) % self.k
            return True
    
    def Front(self):
        return -1 if self.cqueue[self.front] is None else self.cqueue[self.front]
    
    def Rear(self):
        return -1 if self.cqueue[self.rear - 1] is None else self.cqueue[self.rear - 1]
    
    def isEmpty(self):
        return self.front == self.rear and self.cqueue[self.front] is None
    
    def isFull(self):
        return self.front == self.rear and self.cqueue[self.front] is not None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()