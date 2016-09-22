class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.data = vec2d
        self.x = 0
        if self.x < len(self.data):
            self.y = 0
            self.helper()

    def next(self):
        """
        :rtype: int
        """
        val = self.data[self.x][self.y]
        self.y += 1
        self.helper()
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.x < len(self.data) and self.y < len(self.data[self.x])
        
    def helper(self):
        while self.x < len(self.data) and self.y == len(self.data[self.x]):
            self.x += 1
            if self.x < len(self.data):
                self.y = 0

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())