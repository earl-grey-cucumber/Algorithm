class union_find(object):
    def __init__(self, size):
        self.f = [-1] * size
        
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
    def isValid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n
        
    def numIslands2(self, m, n, positions):
        if not positions:
            return []
        result = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        uf = union_find(m * n)
        count = 0
        for p in positions:
            cur = p[0] * n + p[1]
            if uf.f[cur] == -1:
                count += 1
                uf.f[cur] = cur
            for d in directions:
                x, y = p[0] + d[0], p[1] + d[1]
                if self.isValid(x, y, m, n) and uf.merge(cur, x * n + y):
                    count -= 1
            result.append(count)
        return result

 