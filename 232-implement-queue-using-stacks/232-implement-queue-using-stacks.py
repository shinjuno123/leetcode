class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
        
    
    def pop(self):
        self.peek()
        return self.output.pop()
    
    def push(self,x):
        self.input.append(x)
    
    
    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        
        return self.output[-1]
    
    def empty(self):
        return len(self.input) == 0 and len(self.output) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()