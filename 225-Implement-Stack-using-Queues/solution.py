class Stack(object):
    def __init__(self):
        self.q = []
        
    def push(self, x):
        size = len(self.q)
        self.q.append(x)
        while size > 0:
            self.q.append(self.q.pop(0))
            size -= 1
            
    def pop(self):
        return self.q.pop(0)

    def top(self):
        return self.q[0]
        
    def empty(self):
        return len(self.q) == 0
    """
    def __init__(self):
        self.q1, self.q2 = [], []

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        self.q1.pop(0)

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0
    """