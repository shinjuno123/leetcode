class MyCircularQueue:

    def __init__(self, k: int):
        self.cq = [None] * k
        self.front = 0
        self.rear = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.cq[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        return True
            

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.cq[self.front] = None
        self.front = (self.front + 1) % self.k
        return True

    def Front(self) -> int:
        return self.cq[self.front] if self.cq[self.front] is not None else -1

    def Rear(self) -> int:
        return self.cq[self.rear - 1] if self.cq[self.rear - 1] is not None else -1

    def isEmpty(self) -> bool:
        return self.rear == self.front and self.cq[self.front] is None 

    def isFull(self) -> bool:
        return self.rear == self.front and self.cq[self.front] is not None
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()