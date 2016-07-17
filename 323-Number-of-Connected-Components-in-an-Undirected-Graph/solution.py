class union_find(object):
        def __init__(self, n):
            self.f = range(n)
            self.count = n

        def find(self, x):
            if self.f[x] == x:
                return x
            self.f[x] = self.find(self.f[x])
            return self.f[x]

        def merge(self, x, y):
            x = self.find(x)
            y = self.find(y)
            if x != y:
                self.f[x] = y
                self.count -= 1

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = union_find(n)
        for x, y in edges:
            uf.merge(x, y)
        return uf.count
            
            