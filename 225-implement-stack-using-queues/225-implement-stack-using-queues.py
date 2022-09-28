from collections import deque
class MyStack:
    def __init__(self):
        self.queue = deque()
        self.len = 0
    
    def push(self,x):
        self.queue.append(x)
        self.len += 1
    
    def pop(self): 
        if self.len == 0:
            return
        
        for i in range(self.len - 1):
            self.queue.append(self.queue.popleft())
        
        self.len -= 1
        return self.queue.popleft()
    
    def top(self):
        return self.queue[self.len - 1]
    
    
    def empty(self):
        return self.len == 0
    
        
    
    

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()