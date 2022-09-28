class MyQueue:

    def __init__(self):
        self.stack = []
        self.len = 0
    
    
    def push(self,x):
        tmp = []
        for _ in range(self.len):
            tmp.append(self.stack.pop())
        
        self.stack.append(x)
        print(self.stack,tmp)
        
        for _ in range(self.len):
            self.stack.append(tmp.pop())
        
        self.len += 1
        
    def pop(self):
        self.len -= 1
        return self.stack.pop()
    
    
    def peek(self):
        return self.stack[self.len-1]
    
    
    def empty(self):
        return self.len == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()