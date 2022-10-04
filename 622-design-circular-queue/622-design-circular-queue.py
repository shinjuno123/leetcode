class MyCircularQueue:
    
    def __init__(self, k: int):
        self.cqueue = [None] * k
        self.front = 0
        self.rear = 0
        self.len = 0
        self.max = k

    def enQueue(self, value: int) -> bool:
        # if there is space in cqueue
        if self.len < self.max:
            self.cqueue[self.rear] = value
            self.rear = (self.rear + 1) % self.max
            self.len += 1
            return True
        
        return False

    def deQueue(self) -> bool:
        # if cqueue's space is full
        if self.len:
            self.cqueue[self.front] = None
            self.front = (self.front + 1) % self.max
            self.len -= 1
            return True
        
        return False
    

    def Front(self) -> int:
        return self.cqueue[self.front] if self.cqueue[self.front] is not None else -1 

    def Rear(self) -> int:
        return self.cqueue[self.rear - 1] if self.cqueue[self.rear - 1] is not None else -1 

    def isEmpty(self) -> bool:
        return True if self.rear == self.front and self.cqueue[self.front] is None else False

    def isFull(self) -> bool:
        return True if self.rear == self.front and self.cqueue[self.rear] else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()