class UnionFind(object):
    def __init__(self, n):
        self.f = range(n)
        self.count = n
    
    def find_father(self, x):
        if self.f[x] == x:
            return x
        self.f[x] = self.find_father(self.f[x])
        return self.f[x]
        
    def merge(self, x, y):
        x = self.find_father(x)
        y = self.find_father(y)
        if x != y:
            self.f[x] = y
            self.count -= 1
    
class Solution(object):
    def validTree(self, n, edges):
        uf = UnionFind(n)
        for x, y in edges:
            if uf.find_father(x) == uf.find_father(y):
                return False
            uf.merge(x, y)
        return uf.count == 1

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.f[x] = y
            self.count -= 1
   