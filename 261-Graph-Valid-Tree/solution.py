class Solution(object):
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,
        """
        def visit(v):
            map(visit, neighbors.pop(v, []))
        visit(0)
        """
        queue = collections.deque([0])
        while queue:
            queue.extend(neighbors.pop(queue.popleft(), []))
        return not neighbors
        