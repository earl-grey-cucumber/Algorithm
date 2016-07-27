# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        mapping = {}
        if not node:
            return node
        return self.dfs(node, mapping)
                    
    def dfs(self, node, mapping):
        if node in mapping:
            return mapping[node]
        cur = UndirectedGraphNode(node.label)
        mapping[node] = cur
        for n in node.neighbors:
            cur.neighbors.append(self.dfs(n, mapping))
        return cur
                
                