class MyQueue:
    
    def __init__(self):
        self.input = []
        self.output = []
        self.len = 0

    def push(self, x: int) -> None:
        self.input.append(x)
        self.len += 1

    def pop(self) -> int:
        self.peek()
        self.len -= 1
        return self.output.pop()

    def peek(self) -> int:
        if len(self.output) == 0:
            while self.input:
                self.output.append(self.input.pop())
            return self.output[-1]
        else:
            return self.output[-1]

    def empty(self) -> bool:
        return self.len == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()