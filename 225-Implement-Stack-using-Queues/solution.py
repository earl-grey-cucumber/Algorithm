class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1, self.q2 = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        :rtype: nothing
        """
        self.q1.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) == 0