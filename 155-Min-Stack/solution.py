"""
only push the old minimum value when the current minimum value changes after pushing the new value x
if pop operation could result in the changing of the current minimum value, pop twice and change the current minimum value to the last minimum value
"""

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_val = sys.maxint
        
    def push(self, x):
        if x <= self.min_val:
            self.stack.append(self.min_val)
            self.min_val = x
        self.stack.append(x)
        
    def pop(self):
        if self.stack[-1] == self.min_val:
            self.stack.pop(-1)
            self.min_val = self.stack[-1]
            self.stack.pop(-1)
        else:
            self.stack.pop(-1)
        if not self.stack:
            self.min_val = sys.maxint
        
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_val
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()