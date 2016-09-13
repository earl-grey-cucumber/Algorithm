class ZigzagIterator(object):
    """
    def __init__(self, v1, v2):
        self.inputs = []
        self.inputs.append(v1)
        self.inputs.append(v2)
        self.row, self.col = 0, 0
        
    def next(self):
        val = -1
        n = len(self.inputs)
        while self.row < n and self.col >= len(self.inputs[self.row]):
            self.row += 1
        if self.row < n:
            val = self.inputs[self.row][self.col]
        self.row += 1
        while self.row < n and self.col >= len(self.inputs[self.row]):
            self.row += 1
        if self.row >= n:
            self.row = 0
            self.col += 1
        return val

    def hasNext(self):
        return self.col < len(self.inputs[0]) or self.col < len(self.inputs[1])
    """
    def __init__(self, v1, v2):  
        self.queue=[_ for _ in (v1,v2) if _]

    def next(self):
        v=self.queue.pop(0)
        ret=v.pop(0)
        if v: self.queue.append(v)
        return ret

    def hasNext(self):
        return self.queue
        
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())