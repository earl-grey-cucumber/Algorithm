class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_val = None
        
    def push(self, x):
        if not self.stack:
            self.stack.append(0)
            self.min_val = x
        else:
            self.stack.append(x - self.min_val)
            if x < self.min_val:
                self.min_val = x
        
    def pop(self):
        x = self.stack.pop(-1)
        if x < 0:
            self.min_val -= x
        
    def top(self):
        x = self.stack[-1]
        if x > 0:
            return x + self.min_val
        else:
            return self.min_val

    def getMin(self):
        return self.min_val
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()