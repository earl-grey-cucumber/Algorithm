class union_find(object):
    def __init__(self, size):
        self.f = [i for i in range(size)]
        self.count = size
        
    def findFather(self, i):
        if self.f[i] == i:
            return i
        self.f[i] = self.findFather(self.f[i])
        return self.f[i]
        
    def merge(self, x, y):
        if self.f[x] == -1:
            return False
        if self.f[y] == -1:
            return False
        x = self.findFather(x)
        y = self.findFather(y)
        if x == y:
            return False
        else:
            self.f[y] = x
            return True

class Solution(object):
    def countComponents(self, n, edges):
        uf = union_find(n)
        for edge in edges:
            x, y = edge[0], edge[1]
            if uf.merge(x, y):
                uf.count -= 1
        return uf.count
            