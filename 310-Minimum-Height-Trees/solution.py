class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 0:
            return []
        if n == 1:
            return [0]
        result = []
        maps, degrees = {}, {}
        for i in range(n):
            maps[i], degrees[i] = [], 0
        for s, e in edges:
            maps[s].append(e)
            maps[e].append(s)
            degrees[s] += 1
            degrees[e] += 1
        queue, visited = [], set()
        for key in degrees:
            if degrees[key] == 1:
                queue.append(key)
        while n > 2:
            size = len(queue)
            for i in range(size):
                cur = queue.pop(0)
                n -= 1
                for neighbor in maps[cur]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)
                        
        return queue