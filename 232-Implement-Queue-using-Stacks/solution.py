class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1, self.stack2 = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop(0))
        self.stack2.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop(0))
        return self.stack2[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) + len(self.stack2) == 0